# ADR-013 — Porta de invocação técnica de Tools

* **Status:** Accepted
* **Data:** 2026-11-24

## Contexto

O Assist Engine precisa permitir que componentes de domínio utilizem capacidades técnicas disponibilizadas pelo subsistema de Tools. Essa utilização tem natureza diferente da execução estratégica coordenada pelo Decision Engine: o consumidor de domínio já conhece a capacidade necessária e solicita sua invocação diretamente.

O contrato `Executor`, definido para estratégias selecionadas pelo Decision Engine, não representa essa solicitação técnica. Misturar os dois conceitos faria a invocação de uma capacidade parecer uma nova estratégia de execução e poderia levar Business Modules a depender do Tool Engine ou de implementações concretas de Tools.

É necessário definir uma porta que preserve o isolamento do Core e permita reutilizar o mecanismo técnico existente, incluindo validação, execução, retry e tratamento de falhas. A decisão complementa o Sistema de Tools (ADR-006), o princípio de Tools como capacidades (ADR-010), o Core agnóstico a domínio (ADR-007), a Arquitetura Hexagonal (ADR-002) e a comunicação baseada em contratos (ADR-011).

## Alternativas consideradas

**1. Business Modules chamarem implementações concretas de Tools**

Cada Business Module obteria ou instanciaria diretamente as Tools utilizadas. Essa opção foi rejeitada por acoplar módulos de domínio às implementações, contrariando a inversão de dependências e dificultando substituições e testes.

**2. Business Modules receberem o `Result` final do Tool Engine**

O Tool Engine executaria a capacidade e entregaria seu resultado estratégico ao Business Module. Essa opção foi rejeitada porque o `Result` pertence à estratégia de execução: o Tool Engine interpreta o `ToolResult` e consolida um resultado próprio. Ela também retiraria do Business Module a interpretação funcional que cabe às suas regras de domínio.

**3. Criar mecanismos de execução técnica independentes para cada consumidor**

Cada consumidor poderia implementar sua própria localização, validação, execução e política de retry. Essa opção foi rejeitada por duplicar responsabilidades e permitir comportamentos divergentes para a mesma Tool.

**4. Permitir a invocação de ToolFlows pela porta desde a primeira versão**

A porta poderia aceitar Tools individuais e composições de Tools. Essa opção foi rejeitada para manter o escopo inicial explícito e simples. Business Modules poderão invocar Tools individuais; uma necessidade concreta poderá motivar uma decisão futura sobre ToolFlows.

## Decisão

O Assist Engine adotará uma porta independente denominada `ToolInvocationPort` para a invocação técnica de Tools por consumidores que já conhecem a capacidade necessária. Seu contrato conceitual será:

```python
class ToolInvocationPort(Protocol):

    def invoke(
        self,
        tool_id: str,
        parameters: dict[str, object],
    ) -> ToolResult:
        ...
```

A porta utilizará `Protocol`, receberá um identificador estável da Tool e parâmetros estruturados, e retornará `ToolResult`. Ela não exporá implementações concretas, Registry ou mecanismos internos, nem oferecerá métodos adicionais sem necessidade identificada. A Tool será identificada exclusivamente por `tool_id`; cabe ao subsistema de Tools localizar a implementação registrada. Business Modules não dependerão de instâncias concretas.

### Contratos de entrada

Cada Tool declarará seu próprio contrato de entrada, incluindo parâmetros aceitos, tipos, obrigatoriedade, restrições e validações. O mesmo contrato será usado pelo Tool Engine e pela `ToolInvocationPort`; não haverá definições duplicadas por consumidor.

### Falhas de invocação e validação

Falhas esperadas originadas pela própria invocação, como Tool inexistente (`invocation.tool_not_found`) ou parâmetros inválidos (`invocation.invalid_parameters`), serão representadas por `ToolFailureResult`. Elas terão retry desabilitado independentemente das políticas configuradas na Tool; falhas de validação não provocarão a execução da Tool nem novas tentativas. A política de retry aplica-se às falhas produzidas durante a execução técnica da Tool, respeitando sua classificação de retryabilidade e as configurações estabelecidas. Ambos os tipos de falha continuam representados por `ToolFailureResult`, e não serão criadas exceções específicas para essas falhas esperadas. Exceções inesperadas de programação ou infraestrutura continuarão seguindo o mecanismo geral de exceções e não serão consideradas automaticamente falhas técnicas recuperáveis.

### Retry

O retry será responsabilidade exclusiva do subsistema de Tools. Tool Engine e `ToolInvocationPort` usarão o mesmo mecanismo interno de execução e as mesmas políticas:

* retry ficará desabilitado por padrão quando não configurado;
* a Tool determinará a retryabilidade de suas falhas;
* o subsistema de Tools aplicará a política;
* a configuração de ToolFlow poderá sobrescrever a configuração da Tool, quando aplicável;
* Business Modules não executarão retry por conta própria;
* repetições respeitarão a segurança e a idempotência da operação.

### Mecanismo compartilhado e políticas distintas

Tool Engine e `ToolInvocationPort` compartilharão o mecanismo interno do subsistema de Tools: Registry, validação de parâmetros, execução das Tools, retry e tratamento de falhas técnicas. Suas políticas de seleção permanecerão distintas. O Tool Engine recebe `Request` e `Context`, seleciona capacidades por matching determinístico e retorna `Result`. A porta recebe `tool_id` explícito, executa a capacidade solicitada e retorna `ToolResult`.

Não será criado um segundo Tool Engine nem um novo Executor. `Executor` representa uma estratégia de execução escolhida pelo Decision Engine:

```text
execute(request: Request, context: Context) -> Result
```

A invocação técnica é uma solicitação de capacidade por um consumidor que já a conhece:

```text
invoke(tool_id, parameters) -> ToolResult
```

Portanto, `ToolInvocationPort` não representa uma segunda estratégia de execução.

### Interpretação dos resultados

O subsistema de Tools não interpretará regras de negócio. Quando o Tool Engine utilizar uma Tool, ele interpretará o `ToolResult`, produzirá o `Result` final da estratégia e determinará o conteúdo operacional apropriado. Quando um Business Module utilizar uma Tool, o módulo receberá `ToolResult`, aplicará suas regras de domínio, decidirá o significado funcional do resultado e produzirá seu próprio `Result`. A porta técnica nunca retornará `Result`.

### Escopo inicial

`ToolInvocationPort` permitirá somente a invocação de Tools individuais. A invocação de ToolFlows por Business Modules está fora do escopo inicial e poderá ser avaliada futuramente se houver necessidade concreta. O Tool Engine continuará podendo utilizar ToolFlows internamente.

## Fluxos

### Fluxo A — Tool Engine como Executor

```text
Request + Context
    → Decision Engine
    → Tool Engine
    → Matching determinístico
    → Seleção de Tool ou ToolFlow
    → Validação
    → Execução pelo subsistema de Tools
    → ToolResult
    → Tool Engine interpreta e consolida
    → Result
    → Orchestrator
    → ResponseBuilder
```

### Fluxo B — Business Module utilizando Tool

```text
Request + Context
    → Decision Engine
    → Business Module
    → Aplicação das regras de domínio
    → ToolInvocationPort.invoke(tool_id, parameters)
    → Subsistema de Tools
    → Validação e execução
    → ToolResult
    → Business Module interpreta
    → Aplicação das regras de domínio
    → Result
    → Orchestrator
    → ResponseBuilder
```

No fluxo B, a invocação técnica é uma capacidade utilizada pelo Business Module, não uma estratégia adicional selecionada pelo Decision Engine.

## Consequências

### Positivas

* Separa claramente o contrato de execução estratégica do contrato de invocação técnica.
* Reutiliza o mecanismo técnico de Tools e centraliza validação, retry e tratamento de falhas.
* Reduz o acoplamento entre Business Modules e implementações concretas.
* Mantém `ToolResult` e `Result` semanticamente distintos e preserva a interpretação de domínio nos Business Modules.
* Permite compartilhar o mecanismo de execução sem compartilhar políticas de seleção.
* Permite evoluir implementações sem alterar os consumidores que dependem da porta.

### Custos e limitações

* Introduz uma porta adicional e exige manter contratos de entrada das Tools.
* Business Modules precisam conhecer os identificadores das capacidades que utilizam.
* Inicialmente, Business Modules não poderão invocar ToolFlows por essa porta.

## Implementação

Esta ADR registra a arquitetura aprovada; não afirma que a porta ou seu mecanismo já estejam implementados. A implementação ocorrerá posteriormente, nas Sprints correspondentes. Esta decisão não altera contratos existentes nem antecipa a implementação de Business Modules.

## Decisões relacionadas

* [ADR-002 — Arquitetura Hexagonal](ADR-002-hexagonal-architecture.md)
* [ADR-006 — Sistema de Tools](ADR-006-tool-system.md)
* [ADR-007 — O Core não possui conhecimento sobre domínios de negócio](ADR-007-business-agnostic-core.md)
* [ADR-010 — Tools como capacidades](ADR-010-tools-as-capabilities.md)
* [ADR-011 — Orquestração baseada em contratos](ADR-011-contract-based-orchestration.md)
