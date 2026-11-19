# Sprint 2 — Pipeline

- **Fase:** 1 — Fundação
- **Estado:** Concluída
- **Pergunta orientadora:** O fluxo interno consegue ser organizado em etapas independentes?

## Objetivo

Introduzir um Pipeline sequencial composto por etapas independentes, com propagação do contexto e tratamento observável de falhas.

## Missões

- Pipeline.
- PipelineStep.
- Context Builder.
- Response Builder.
- Logging.
- Tratamento de exceções.

## Entrega esperada

Pipeline totalmente funcional.

## Resultado alcançado

A implementação executa instâncias de `PipelineStep` em sequência, encaminha o `Context` retornado por cada etapa, registra início, execução, conclusão e falhas, e converte erros de etapa em `PipelineStepError`. O `ContextBuilder` cria um contexto vazio. Os testes existentes cobrem a ordem de execução, a propagação do contexto, a interrupção diante de falhas e um fluxo de integração com um `PipelineStep` de teste.

A entrega é funcional no escopo básico do Pipeline implementado. Há limitações que permanecem para evolução: não existe implementação concreta de `PipelineStep` em `system/src/`; `ResponseBuilder` retorna o próprio `Context` em vez de construir uma `Response`, como prevê a documentação arquitetural; e o Pipeline ainda não está integrado ao Orchestrator. O planejamento original da Sprint chamava a missão de Middleware; após a revisão conceitual, este registro usa `PipelineStep` para a abstração implementada. Middleware permanece um conceito distinto, reservado a uma necessidade futura concreta de interceptação ou composição da execução. Portanto, a Sprint não representa a implementação completa de todos os componentes e fluxos previstos na arquitetura do Assist Engine.
