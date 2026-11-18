# Assist Engine — Diretrizes para Agentes

## 1. Visão geral

O Assist Engine é um motor de agentes de Inteligência Artificial desenvolvido com foco em modularidade, extensibilidade e independência de provedores e canais de comunicação.

Sua arquitetura busca separar responsabilidades, preservar o isolamento do Core e permitir a evolução independente de seus componentes.

### Filosofia fundamental

> A IA não é o sistema. É apenas uma capacidade que o sistema pode utilizar quando necessário.

O sistema deve priorizar regras determinísticas, contratos explícitos e ferramentas convencionais. A utilização de Inteligência Artificial deve ocorrer quando as abordagens determinísticas não forem suficientes.

## 2. Fontes de verdade

Antes de implementar funcionalidades ou propor alterações arquiteturais, consulte a documentação pertinente.

| Documento | Responsabilidade |
|---|---|
| `README.md` | Apresentação, configuração e utilização do projeto. |
| `docs/adr/` | Registro das decisões arquiteturais aprovadas. |
| `docs/architecture/` | Especificação da arquitetura, componentes, fluxos e dependências. |
| `docs/sprints/` | Planejamento e histórico das entregas. |
| `docs/project-status.md` | Estado atual, funcionalidades implementadas e pendências. |

Em caso de divergência entre documentação e implementação:

1. Identifique a divergência.
2. Verifique as ADRs e decisões arquiteturais relacionadas.
3. Não altere silenciosamente uma decisão arquitetural.
4. Apresente a divergência e proponha uma solução antes de realizar mudanças que afetem contratos ou responsabilidades.

Este arquivo reúne orientações de trabalho. Consulte as fontes de verdade acima para detalhes de decisões e contratos; não replique seu conteúdo aqui.

## 3. Organização do projeto

O repositório possui duas áreas principais:

- `system/`: implementação executável do Assist Engine.
- `docs/`: documentação arquitetural, decisões e planejamento do projeto.

O código-fonte e os testes devem permanecer organizados dentro de `system/`.

Respeite a separação de responsabilidades existente e evite introduzir novos diretórios ou abstrações sem necessidade concreta. Antes de criar módulos, examine a estrutura existente e identifique onde a nova responsabilidade deve residir.

## 4. Princípios arquiteturais

### Arquitetura Hexagonal e isolamento do Core

- Preserve o isolamento do Core: a lógica central não deve depender de detalhes de infraestrutura.
- Introduza dependências externas por meio de abstrações e contratos.
- Implemente integrações nas camadas apropriadas, sem contaminar o domínio.
- Consulte a ADR-002 e a documentação arquitetural para conhecer os limites de dependência.

### Independência de provedores e canais

- O Core não deve depender diretamente de SDKs de provedores de IA nem de implementações específicas de memória.
- Provedores devem ser substituíveis sem exigir alterações na lógica de negócio do Core; respeite os contratos de cada capacidade.
- O motor não deve conhecer os canais responsáveis por receber ou entregar mensagens.
- Não introduza regras específicas de canais no domínio; mantenha a comunicação entre componentes desacoplada.
- Consulte as ADRs-004 e 005 para decisões sobre provedores.

### Orquestração e Pipeline

- O Orchestrator deve coordenar o processamento por contratos explícitos, sem conhecer implementações concretas desnecessariamente.
- Evite dependências diretas entre componentes que devem permanecer independentes.
- Preserve o Pipeline como mecanismo sequencial e extensível. Novas etapas devem respeitar os contratos e a ordem de execução definida.
- Não coloque responsabilidades de orquestração dentro de etapas individuais. Mantenha separadas a construção do contexto, o processamento e a construção da resposta.
- Consulte as ADRs-008 e 011 e a documentação arquitetural correspondente.

### Inteligência Artificial e ferramentas

- Priorize soluções determinísticas e utilize IA quando elas forem insuficientes.
- Mantenha a capacidade de IA desacoplada dos componentes que a consomem.
- Trate Tools como capacidades disponibilizadas ao motor. Preserve a distinção entre a definição de uma ferramenta e sua implementação e mantenha desacoplado o mecanismo de utilização das ferramentas concretas.
- Consulte as ADRs-006, 009 e 010 para as decisões relacionadas.

## 5. Convenções de desenvolvimento

O projeto utiliza Python.

- Utilize type hints em funções, métodos e contratos.
- Prefira funções e métodos com responsabilidades bem definidas.
- Utilize `snake_case` para módulos, funções e variáveis e `PascalCase` para classes.
- Evite dependências desnecessárias, efeitos colaterais ocultos e abstrações sem necessidade identificada.
- Preserve a simplicidade, a legibilidade e os comportamentos existentes.
- Para modelos de domínio, respeite os padrões de imutabilidade e as decisões já estabelecidas.
- Não altere contratos existentes apenas para facilitar uma implementação específica.

## 6. Testes e qualidade

Todo novo comportamento deve ter testes compatíveis com sua responsabilidade. Mantenha os testes em `system/tests/`.

- Testes unitários devem validar comportamentos isoladamente.
- Testes de integração devem validar a interação entre componentes.
- Não coloque testes manuais ou funções de teste em arquivos de produção.
- Não remova testes existentes para fazer uma implementação passar nem reduza cenários sem justificativa.

Execute os testes pertinentes e, quando possível, a suíte completa a partir de `system/` com `pytest`. Analise eventuais falhas e informe os resultados obtidos. Nunca declare testes como aprovados sem executá-los.

## 7. Governança de ADRs

Consulte as ADRs existentes antes de propor uma nova decisão. Evite duplicar decisões já registradas e não altere silenciosamente uma decisão aprovada.

Considere uma nova ADR quando a alteração introduzir tecnologia ou dependência estrutural, modificar contratos ou responsabilidades, alterar a direção das dependências, introduzir uma estratégia de integração ou modificar significativamente uma decisão arquitetural existente.

Siga o padrão documental existente. Registre a decisão, as justificativas, as alternativas consideradas e as consequências relevantes; a ADR deve registrar a decisão, não o passo a passo da implementação.

## 8. Documentação

Mantenha a documentação alinhada à evolução real do sistema. Se uma implementação alterar significativamente a arquitetura, atualize os documentos arquiteturais afetados, a estrutura do projeto quando novos módulos forem introduzidos, o status do projeto e os registros das Sprints correspondentes, conforme aplicável.

Evite duplicar informações: cada documento deve ter responsabilidade clara e apontar para outras fontes quando necessário.

## 9. Processo de trabalho

Antes de implementar:

1. Examine os arquivos relacionados à tarefa.
2. Consulte as ADRs e os documentos arquiteturais pertinentes.
3. Identifique contratos, responsabilidades e impactos em componentes e testes.
4. Verifique se a solução respeita a arquitetura existente.

Durante o trabalho, faça alterações pequenas e coerentes, preserve comportamentos existentes, não amplie o escopo sem autorização, não introduza dependências sem justificativa e não modifique arquivos não relacionados à tarefa.

Ao concluir, apresente um resumo das alterações e dos arquivos criados ou modificados, informe os testes executados e seus resultados, registre eventuais pendências e indique se a documentação precisa de atualização.

## 10. Princípio final

Toda evolução do Assist Engine deve preservar o isolamento do Core, a inversão de dependências, a comunicação por contratos, a independência de provedores e canais, as responsabilidades bem definidas, o uso de IA como último recurso e a simplicidade com extensibilidade.

Na dúvida, consulte a documentação, identifique as implicações arquiteturais e apresente uma proposta antes de introduzir mudanças estruturais.
