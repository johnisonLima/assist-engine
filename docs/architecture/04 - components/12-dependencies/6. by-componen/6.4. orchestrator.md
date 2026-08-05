# Orchestrator

---

# Objetivo

Este documento define as dependências permitidas e proibidas do Orchestrator.

Seu objetivo é garantir que o Orchestrator permaneça exclusivamente responsável pela coordenação do fluxo arquitetural, preservando sua independência em relação às implementações concretas dos componentes do Assist Engine.

As regras aqui descritas complementam a documentação do componente, especificando exclusivamente seus relacionamentos arquiteturais.

---

# Visão Geral

O Orchestrator ocupa a posição central do Core.

Embora coordene praticamente todo o fluxo interno da arquitetura, seu conhecimento limita-se aos contratos dos componentes envolvidos no processamento.

```mermaid
flowchart LR

Pipeline

-->

Orchestrator

-->

Decision

-->

Executor

-->

Response
```

Essa posição não autoriza o Orchestrator a conhecer implementações concretas.

Seu papel é exclusivamente coordenar.

---

# Dependências Permitidas

O Orchestrator pode conhecer apenas os seguintes elementos.

| Dependência                                  | Tipo     | Justificativa                          |
| -------------------------------------------- | -------- | -------------------------------------- |
| Pipeline                                     | Contrato | Recebimento da requisição preparada.   |
| Decision Engine                              | Contrato | Solicitação da estratégia de execução. |
| Executor                                     | Contrato | Execução da estratégia selecionada.    |
| Response Builder                             | Contrato | Construção da resposta padronizada.    |
| Modelos internos (Request, Result, Response) | Contrato | Coordenação do fluxo arquitetural.     |

O Orchestrator nunca deve depender de implementações concretas.

---

# Dependências Proibidas

O Orchestrator nunca deve conhecer diretamente:

| Componente          | Motivo                                           |
| ------------------- | ------------------------------------------------ |
| Communication Layer | Infraestrutura não pertence ao Core.             |
| Adapter Layer       | Conversão de formatos pertence à infraestrutura. |
| Rule Engine         | Deve conhecer apenas o contrato do Executor.     |
| Tool Engine         | Deve conhecer apenas o contrato do Executor.     |
| AI Engine           | Deve conhecer apenas o contrato do Executor.     |
| Business Modules    | Deve conhecer apenas o contrato do Executor.     |
| AI Providers        | Implementações pertencem à infraestrutura.       |
| Tools               | Capacidades são abstraídas pelo Tool Engine.     |

Essas restrições preservam o baixo acoplamento entre o Core e suas implementações.

---

# Comunicação Permitida

O Orchestrator comunica-se apenas com contratos arquiteturais.

```mermaid
flowchart LR

Pipeline

-->

IOrchestrator

-->

IDecisionEngine

-->

IExecutor

-->

IResponseBuilder
```

Nenhuma comunicação direta com implementações concretas é permitida.

---

# Comunicação por Contratos

Todas as dependências do Orchestrator devem ocorrer por abstrações definidas pelo Core.

Exemplos:

```text
IOrchestrator

IDecisionEngine

IExecutor

IResponseBuilder
```

Essa abordagem permite substituir qualquer implementação sem modificar o Orchestrator.

A coordenação do fluxo permanece completamente independente das tecnologias utilizadas.

---

# Fluxo Arquitetural

O Orchestrator atua como coordenador do processamento interno.

```mermaid
flowchart LR

Pipeline

-->

Orchestrator

-->

Decision

-->

Executor

-->

ResponseBuilder["Response Builder"]
```

O componente nunca altera esse fluxo.

Seu papel limita-se a coordenar sua execução.

---

# Restrições Arquiteturais

O Orchestrator deve obedecer às seguintes restrições.

* Nunca tomar decisões arquiteturais.
* Nunca executar regras de negócio.
* Nunca executar Tools.
* Nunca comunicar-se com AI Providers.
* Nunca construir respostas.
* Nunca conhecer implementações concretas.
* Nunca modificar a estratégia selecionada pelo Decision Engine.

Sua única responsabilidade é coordenar o fluxo do Core.

---

# Justificativa Arquitetural

O Orchestrator representa o ponto central de coordenação da arquitetura.

Naturalmente, ele precisa conhecer mais contratos do que qualquer outro componente.

Entretanto, esse conhecimento permanece limitado às abstrações definidas pelo Core.

Essa decisão impede que o Orchestrator se transforme em um componente excessivamente acoplado, preservando sua simplicidade e facilitando a evolução da arquitetura.

---

# Checklist Arquitetural

Antes de adicionar uma nova dependência ao Orchestrator, responda às seguintes perguntas:

* Essa dependência representa apenas um contrato?
* O Orchestrator realmente precisa conhecê-la?
* Ela altera a responsabilidade de coordenação?
* Ela introduz conhecimento sobre infraestrutura?
* Ela conhece uma implementação concreta?

Caso alguma resposta seja positiva para as duas últimas perguntas, a dependência não deve ser adicionada.

---

# Considerações Finais

O Orchestrator possui o maior número de relacionamentos arquiteturais do Assist Engine.

Entretanto, essas relações ocorrem exclusivamente por meio de contratos, preservando a independência entre coordenação e execução.

Esse princípio garante que o Core permaneça desacoplado das implementações concretas e permite que novos executores, estratégias e tecnologias sejam incorporados ao sistema sem alterar o componente responsável por coordenar o fluxo arquitetural.
