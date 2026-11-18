# Estado do Projeto — Assist Engine

**Última atualização:** 2026-11-18
**Escopo:** fotografia do estado verificável no repositório nesta data. Consulte as ADRs e a documentação arquitetural para decisões e contratos completos.

## 1. Visão geral

O Assist Engine é um motor reutilizável para construção de assistentes inteligentes, com a intenção de atender diferentes canais e provedores por meio de um Core desacoplado. A filosofia do projeto é que **a IA não é o sistema**: deve ser uma capacidade utilizada quando os mecanismos determinísticos não forem suficientes.

O desenvolvimento está em estágio inicial. O repositório registra como concluídas a Sprint 1 (Core) e a Sprint 2 (Pipeline). A implementação contém modelos básicos de domínio, um Orchestrator simples e uma infraestrutura inicial de Pipeline. A maior parte dos componentes previstos na arquitetura — como Decision Engine, Tools, provedores de IA, memória, adapters e módulos de negócio — ainda não está implementada em `system/src/`.

## 2. Estado das Sprints

| Sprint | Estado | Evidência e observações |
|---|---|---|
| Sprint 1 — Core | Concluída | Estado informado no histórico de planejamento fornecido para este documento; a implementação contém `Message`, `Context`, `Response` e `Orchestrator`. |
| Sprint 2 — Pipeline | Concluída | Estado informado no histórico de planejamento fornecido; o repositório contém `Pipeline`, contrato `Middleware`, `ContextBuilder`, `ResponseBuilder` e testes de Pipeline. |
| Próximas Sprints | Planejamento não localizado | Não há diretório `docs/sprints/`, arquivos de Sprint rastreados ou plano de Sprints no repositório. O README contém um roadmap geral, mas não atribui os itens a Sprints nem define datas. |

## 3. Componentes implementados

Estados abaixo refletem a existência de implementação em `system/src/`; “parcial” indica que há código, mas seu comportamento é inicial ou não corresponde integralmente ao papel descrito na arquitetura.

| Componente | Estado | Responsabilidade observada na implementação |
|---|---|---|
| Domain — `Message` | Implementado | Modelo imutável com conteúdo, papel e UUID; rejeita conteúdo vazio ou composto apenas por espaços. |
| Domain — `Response` | Implementado | Modelo imutável com conteúdo e UUID; rejeita conteúdo vazio ou composto apenas por espaços. |
| Domain — `Context` | Implementado, mínimo | Dataclass imutável sem campos, conforme o contexto de execução inicialmente vazio descrito na ADR-012. |
| Application — `Orchestrator` | Implementado, mínimo | Recebe `Message` e `Context` e retorna uma resposta fixa de confirmação que inclui o conteúdo da mensagem. Não coordena ainda o fluxo amplo descrito na arquitetura. |
| Pipeline | Implementado, inicial | Executa uma sequência ordenada de `Middleware`, propaga o `Context` e converte falhas em `MiddlewareError`. |
| Middleware | Contrato implementado | Define `execute(Context) -> Context`. Não há implementação concreta de Middleware em `system/src/`; as implementações de exemplo estão nos testes. |
| `ContextBuilder` | Implementado, mínimo | Cria um `Context` vazio. |
| `ResponseBuilder` | Implementado, placeholder | Retorna o mesmo `Context` recebido. A arquitetura especifica que o componente deve construir e retornar uma `Response`. |
| Logging e exceções do Pipeline | Implementados | O Pipeline registra início, execução, falha e conclusão; expõe `PipelineError` e `MiddlewareError`. |
| Entry point — `system/src/main.py` | Implementado, demonstrativo | Cria uma mensagem, invoca o Orchestrator e imprime a resposta. Também contém uma função de teste manual executada ao importar/executar o módulo. |

Não foram encontrados em `system/src/` implementações de Communication Layer/Adapter, Decision Engine, Rule Engine, Tool Engine/Tools, AI Engine/provedores, memória, RAG, Business Modules ou integração FastAPI. A ADR-003 registra FastAPI como decisão arquitetural, mas isso não comprova implementação do framework.

## 4. Testes e validação

A estratégia documentada é usar testes unitários para comportamentos isolados e testes de integração para interações entre componentes. Os testes automatizados estão organizados em `system/tests/` e utilizam pytest.

Os arquivos existentes cobrem:

- criação de `Context` pelo `ContextBuilder`;
- execução do Pipeline em ordem, propagação do contexto, encapsulamento de falhas e interrupção após falha;
- fluxo de integração entre `ContextBuilder`, Pipeline, middleware de teste e `ResponseBuilder`.

Não há arquivos de teste específicos para os modelos de Domain ou para o Application/Orchestrator. `system/src/main.py` contém uma verificação manual do Orchestrator, mas ela não está organizada como teste pytest em `system/tests/`.

Nenhum resultado de execução de pytest ou métrica de cobertura foi localizado nas fontes consultadas. Portanto, o estado de aprovação da suíte e a cobertura percentual não estão verificados neste documento.

## 5. Decisões arquiteturais

As principais decisões registradas são:

- Objetivo do motor independente de canais, provedores e domínios: [ADR-001](adr/ADR-001-project-purpose.md) e [ADR-007](adr/ADR-007-business-agnostic-core.md).
- Arquitetura Hexagonal e independência do Core: [ADR-002](adr/ADR-002-hexagonal-architecture.md).
- FastAPI como framework de entrada: [ADR-003](adr/ADR-003-fastapi.md).
- Abstrações para provedores de IA e memória: [ADR-004](adr/ADR-004-ai-provider.md) e [ADR-005](adr/ADR-005-memory-abstraction.md).
- Sistema de Tools e IA como último recurso: [ADR-006](adr/ADR-006-tool-system.md) e [ADR-009](adr/ADR-009-ai-last-resort.md).
- Pipeline composto por etapas especializadas e orquestração baseada em contratos: [ADR-008](adr/ADR-008-pipeline-steps.md) e [ADR-011](adr/ADR-011-contract-based-orchestration.md).
- `Context` como contexto de execução, separado de memória conversacional: [ADR-012](adr/ADR-012-context-as-execution-context.md).

A [ADR-010](adr/ADR-010-tools-as-capabilities.md) está presente no repositório, mas seu arquivo está vazio; não há decisão ou status legível a resumir.

## 6. Pendências técnicas

As prioridades abaixo indicam impacto na consistência entre o estado documentado e a implementação, não uma estimativa de esforço.

| Prioridade | Pendência observada | Evidência |
|---|---|---|
| Alta | Alinhar o contrato do `ResponseBuilder` entre código e arquitetura. | `system/src/core/pipeline/response_builder.py` retorna `Context`; `docs/architecture/04-components/11-response-builder.md` define saída `Response`. |
| Alta | Esclarecer e alinhar o papel do Orchestrator e a orquestração por contratos. | O Orchestrator atual apenas formata uma resposta e não recebe Pipeline ou outros componentes por contrato; a ADR-011 e a documentação do Orchestrator descrevem coordenação mais ampla. |
| Média | Definir terminologia/contrato de `Pipeline Steps` versus `Middleware`. | A ADR-008 usa `Pipeline Steps`; a implementação e seus testes usam `Middleware`. A relação entre os termos não está explicitada no código consultado. |
| Média | Completar a ADR-010 ou esclarecer sua relação com a ADR-006. | `ADR-010-tools-as-capabilities.md` está vazio; a ADR-006 registra uma decisão sobre o Sistema de Tools. |
| Média | Atualizar a documentação de estrutura para refletir a implementação atual. | `docs/architecture/07-project-structure.md` descreve `contracts/` e `src/tests/`, e afirma que ainda não há contratos concretos; a implementação atual contém `core/pipeline/`, os testes estão em `system/tests/` e não existe `core/contracts/`. |
| Média | Criar cobertura automatizada específica para Domain e Application, se esses comportamentos permanecerem parte do escopo. | Não há testes correspondentes em `system/tests/`; o único exercício do Orchestrator é uma verificação manual em `system/src/main.py`. |
| Baixa | Remover ou realocar a verificação manual de teste do entry point. | `system/src/main.py` define e chama `test_orchestrator_processes_message()` no próprio arquivo de produção. |
| Média | Reconciliar o escopo da arquitetura v1 com o estágio de implementação. | A documentação arquitetural apresenta diversos componentes como arquitetura estável; a implementação atual contém somente os modelos básicos, Orchestrator simples e Pipeline inicial descritos acima. |

As prioridades não implicam que as capacidades ausentes devam ser implementadas imediatamente; registram apenas inconsistências e lacunas comprovadas. A ADR-010 permanece **aguardando esclarecimento** quanto ao conteúdo pretendido, pois o arquivo vazio não permite determinar se a decisão foi aprovada, substituída ou ainda está em elaboração.

## 7. Próximos marcos

Não foi encontrado planejamento de Sprints futuras. Os objetivos abaixo aparecem no roadmap do [README](../README.md), mas não estão associados a uma Sprint, data ou compromisso de entrega:

- estruturar a arquitetura e evoluir o Core;
- implementar adaptadores de canais;
- implementar memória conversacional;
- criar sistema de intenções e ferramentas;
- integrar banco de dados e RAG;
- integrar provedores de IA, incluindo modelos locais;
- evoluir o uso do motor por diferentes canais.

Este documento deve ser atualizado quando novas Sprints forem planejadas ou concluídas, quando funcionalidades forem implementadas e quando as fontes de planejamento ou arquitetura forem revisadas.
