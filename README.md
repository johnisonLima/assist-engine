# Assist Engine

> Um motor moderno para construção de assistentes inteligentes multicanal.

## Visão Geral

O Assist Engine nasceu como um projeto de estudos sobre arquiteturas modernas para assistentes virtuais baseados em Inteligência Artificial.

O objetivo não é desenvolver apenas um chatbot, mas construir um núcleo inteligente capaz de atender diferentes canais de comunicação utilizando a mesma lógica de processamento.

A arquitetura foi pensada para separar completamente o canal de comunicação da lógica de negócio, permitindo que um único mecanismo de atendimento funcione em aplicações Web, WhatsApp, Instagram, Telegram ou qualquer outro meio.

---

## Objetivos

* Desenvolver uma arquitetura desacoplada para assistentes virtuais.
* Compreender o funcionamento interno de sistemas conversacionais modernos.
* Integrar Inteligência Artificial apenas quando necessário.
* Reduzir custos com consumo de tokens.
* Criar um núcleo reutilizável para diferentes projetos.
* Implementar memória de conversação.
* Utilizar ferramentas (Tools) para execução de ações.
* Implementar consultas em banco de dados.
* Integrar mecanismos de RAG (Retrieval-Augmented Generation).
* Permitir troca de provedores de IA sem alterações na aplicação.

---

## Filosofia

O Assist Engine parte de uma ideia simples:

> A IA não é o sistema.

Ela é apenas um dos componentes responsáveis por interpretar linguagem natural.

Todo o restante da aplicação continua sendo responsabilidade da engenharia de software.

---

## Princípios do Projeto

* Arquitetura modular
* Baixo acoplamento
* Alta coesão
* Independência de plataforma
* Independência do modelo de IA
* Facilidade para testes
* Facilidade para manutenção
* Escalabilidade
* Evolução incremental

---

## Arquitetura (Visão Inicial)

```text
                Canais

 WhatsApp | Instagram | Telegram | Web

                  │

             Adaptadores

                  │

             Assist Engine

        ┌─────────┼─────────┐
        │         │         │
      Core      Memory    Tools
        │
      Intents
        │
       Rules
        │
        AI
        │
  OpenAI | Claude | Gemini | Ollama

                  │

        Banco de Dados / APIs
```

---

## Tecnologias (planejamento inicial)

Backend

* Python
* FastAPI

Banco de Dados

* PostgreSQL

ORM

* SQLAlchemy

Cache

* Redis

Modelos de IA

* OpenAI
* Claude
* Gemini
* Ollama

Vetores

* ChromaDB (inicialmente)

Containers

* Docker

Testes

* Pytest

---

## Roadmap

* [ ] Estruturar arquitetura do projeto
* [ ] Criar núcleo do Assist Engine
* [ ] Implementar adaptador Web
* [ ] Implementar memória de conversação
* [ ] Criar sistema de intenções
* [ ] Implementar sistema de ferramentas
* [ ] Criar integração com banco de dados
* [ ] Implementar RAG
* [ ] Integrar OpenAI
* [ ] Integrar modelos locais
* [ ] Criar adaptador WhatsApp
* [ ] Criar adaptador Telegram
* [ ] Criar adaptador Instagram

---

## Objetivo Final

Ao final do projeto, o Assist Engine deverá ser capaz de atuar como uma plataforma completa para desenvolvimento de assistentes inteligentes, permitindo que novos canais de comunicação, modelos de IA e funcionalidades sejam adicionados sem modificar seu núcleo principal.
