# Planejamento das Sprints — Assist Engine

Este documento apresenta o planejamento geral do Assist Engine, organizado em sete fases e quinze Sprints. As Sprints 1 e 2 estão concluídas; as Sprints 3 a 15 estão planejadas. O planejamento não define datas ou estimativas.

## Fase 1 — Fundação

### Sprint 1 — Core

- **Estado:** Concluída
- **Pergunta:** O Assist Engine consegue processar uma mensagem?
- **Missões:** Estrutura do projeto; `Message`; `Response`; `Context`; `Orchestrator`; primeiro fluxo ponta a ponta.
- **Entrega esperada:** Uma mensagem entra no Core e retorna uma resposta.
- **Restrições:** Sem IA, sem memória e sem tools.

### Sprint 2 — Pipeline

- **Estado:** Concluída
- **Pergunta:** O fluxo interno consegue ser organizado em etapas independentes?
- **Missões:** Pipeline; PipelineStep; Context Builder; Response Builder; Logging; tratamento de exceções.
- **Entrega esperada:** Pipeline totalmente funcional.

## Fase 2 — Inteligência Artificial

### Sprint 3 — AI Provider

- **Estado:** Planejada
- **Pergunta:** O Core consegue conversar com um modelo de IA?
- **Missões:** `IAIProvider`; OpenAI Provider; configuração; integração com Orchestrator; testes básicos.
- **Entrega esperada:** Primeira conversa utilizando IA.

### Sprint 4 — Tool Engine

- **Estado:** Planejada
- **Pergunta:** A IA consegue executar ferramentas?
- **Missões:** `ITool`; Tool Registry; Tool Engine; primeira Tool; Tool Result.
- **Entrega esperada:** A IA chama uma Tool e utiliza seu resultado na resposta.

## Fase 3 — Memória

### Sprint 5 — Memory Provider

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue lembrar da conversa?
- **Missões:** `IMemoryProvider`; Conversation Memory; Context Recovery; persistência inicial; integração com Orchestrator.
- **Entrega esperada:** Memória conversacional funcionando.

## Fase 4 — Conhecimento

### Sprint 6 — RAG

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue responder utilizando conhecimento externo?
- **Missões:** `IRagProvider`; Embeddings; Vector Store; Retrieval; Context Injection.
- **Entrega esperada:** Primeira resposta utilizando documentos externos.

## Fase 5 — Providers

### Sprint 7 — Data Provider

- **Estado:** Planejada
- **Pergunta:** O domínio consegue acessar dados sem depender da tecnologia?
- **Missões:** `IDataProvider`; primeiro Provider; repositórios; mapeamentos; testes.
- **Entrega esperada:** Camada de dados desacoplada do Core.

## Fase 6 — Comunicação

### Sprint 8 — API

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue ser acessado externamente?
- **Missões:** Adapter HTTP; endpoint Chat; serialização; tratamento de erros.
- **Entrega esperada:** Primeira API funcional.

### Sprint 9 — CLI

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue ser utilizado pelo terminal?
- **Missões:** CLI Adapter; entrada; saída; configuração.
- **Entrega esperada:** Assistente funcionando via terminal.

### Sprint 10 — Web

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue ser utilizado por uma interface web?
- **Missões:** Adapter Web; interface mínima; integração.
- **Entrega esperada:** Primeira interface web.

### Sprint 11 — WhatsApp

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue conversar pelo WhatsApp?
- **Missões:** Adapter; Webhook; conversação.
- **Entrega esperada:** Primeira integração oficial.

### Sprint 12 — Telegram

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue conversar pelo Telegram?
- **Missões:** Adapter; Bot; conversação.
- **Entrega esperada:** Integração com Telegram.

## Fase 7 — Evolução

### Sprint 13 — Observabilidade

- **Estado:** Planejada
- **Pergunta:** O sistema consegue ser monitorado?
- **Missões:** Logging estruturado; métricas; tracing.
- **Entrega esperada:** Monitoramento básico.

### Sprint 14 — Novos Providers

- **Estado:** Planejada
- **Missões:** Claude; Gemini; Ollama.
- **Entrega esperada:** Múltiplos modelos suportados.

### Sprint 15 — Plugins

- **Estado:** Planejada
- **Pergunta:** O Assist Engine consegue ser estendido sem alterar o Core?
- **Missões:** Plugin System; descoberta; registro; carregamento.
- **Entrega esperada:** Primeiro plugin externo.

## Registros das Sprints concluídas

- [Sprint 1 — Core](sprint-01-core.md)
- [Sprint 2 — Pipeline](sprint-02-pipeline.md)

Os arquivos individuais registram o escopo e o resultado observado das Sprints concluídas. Este planejamento deve ser atualizado quando o estado das Sprints mudar; novas Sprints só devem receber registros individuais quando forem concluídas.
