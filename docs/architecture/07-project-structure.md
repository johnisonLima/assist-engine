# Project Structure

Este documento descreve a estrutura atual do projeto Assist Engine, apresentando a organização dos diretórios e os principais componentes implementados até o momento.

A estrutura é evolutiva e não representa uma definição definitiva de toda a arquitetura física do projeto. Novos diretórios e componentes devem ser introduzidos conforme novas responsabilidades surgirem durante o desenvolvimento.

## Current Structure

```text
src/
├── core/
│   ├── application/
│   │   ├── __init__.py
│   │   └── orchestrator.py
│   │
│   ├── contracts/
│   │   └── __init__.py
│   │
│   └── domain/
│       ├── __init__.py
│       ├── context.py
│       ├── message.py
│       └── response.py
│
└── tests/
    └── __init__.py
```

## Directories

### `src/`

Contém o código-fonte do Assist Engine.

### `src/core/`

Representa o núcleo do sistema. Contém os componentes responsáveis pelo processamento fundamental de mensagens, sem dependência de canais externos, provedores de IA, memória ou ferramentas.

### `src/core/domain/`

Contém os modelos fundamentais utilizados pelo Core.

Atualmente, possui:

* `message.py` — representa uma mensagem recebida ou produzida pelo sistema, contendo seu identificador, papel e conteúdo.
* `response.py` — representa o resultado produzido pelo processamento de uma mensagem.
* `context.py` — representa o contexto de execução de uma operação do Core. Atualmente não possui dados próprios e será evoluído conforme novas necessidades surgirem.

### `src/core/application/`

Contém componentes responsáveis pela coordenação do processamento dentro do Core.

Atualmente, possui:

* `orchestrator.py` — coordena o processamento de uma `Message` utilizando um `Context` e produzindo uma `Response`.

### `src/core/contracts/`

Destinado aos contratos e abstrações que serão utilizados para desacoplar componentes do Core e suas implementações.

Na Sprint 1, ainda não possui contratos concretos.

### `src/tests/`

Contém os testes relacionados ao sistema.

Os testes serão introduzidos e organizados conforme os comportamentos relevantes de cada etapa do projeto forem implementados.

## Current Core Flow

A estrutura atual permite o primeiro fluxo funcional do Assist Engine:

```text
Message
   ↓
Context
   ↓
Orchestrator
   ↓
Response
```

Esse fluxo representa a primeira validação do Core: uma mensagem pode entrar no sistema, ser processada pelo `Orchestrator` e resultar em uma resposta.

## Evolution

A estrutura apresentada neste documento deve ser atualizada ao final das Sprints quando novas responsabilidades forem incorporadas ao sistema.

A criação de novos diretórios deve ocorrer como consequência de uma necessidade concreta do projeto, evitando a antecipação de estruturas para funcionalidades que ainda não foram implementadas.
