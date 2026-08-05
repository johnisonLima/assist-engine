# Response Builder

---

# Objetivo

Este documento define as dependências permitidas e proibidas do Response Builder.

Seu objetivo é garantir que o Response Builder permaneça exclusivamente responsável pela construção da resposta padronizada do Assist Engine, preservando sua independência em relação aos executores, à infraestrutura e às implementações concretas.

As regras aqui descritas complementam a documentação do componente, especificando exclusivamente seus relacionamentos arquiteturais.

---

# Visão Geral

O Response Builder representa a última etapa do Core.

Sua responsabilidade consiste em transformar um **Result** em uma **Response**, estabelecendo o contrato oficial de saída do Assist Engine.

```mermaid
flowchart LR

Result

-->

ResponseBuilder

-->

Response
```

O Response Builder não possui conhecimento sobre a origem do resultado recebido.

---

# Dependências Permitidas

O Response Builder pode conhecer apenas os seguintes elementos.

| Dependência                                      | Tipo     | Justificativa                                                      |
| ------------------------------------------------ | -------- | ------------------------------------------------------------------ |
| Modelo `Result`                                  | Contrato | Representação padronizada do resultado produzido pelos executores. |
| Modelo `Response`                                | Contrato | Construção da resposta oficial do Core.                            |
| Componentes auxiliares de composição da resposta | Contrato | Organização da Response antes do retorno ao Adapter Layer.         |

Nenhuma dependência relacionada aos executores ou à infraestrutura é necessária.

---

# Dependências Proibidas

O Response Builder nunca deve conhecer diretamente:

| Componente          | Motivo                                            |
| ------------------- | ------------------------------------------------- |
| Communication Layer | A comunicação pertence à infraestrutura.          |
| Adapter Layer       | A adaptação ocorre após a construção da Response. |
| Pipeline            | A preparação da requisição já foi concluída.      |
| Orchestrator        | O fluxo é coordenado externamente.                |
| Decision Engine     | A estratégia já foi executada.                    |
| Rule Engine         | O Response Builder conhece apenas o Result.       |
| Tool Engine         | O Response Builder conhece apenas o Result.       |
| AI Engine           | O Response Builder conhece apenas o Result.       |
| Business Modules    | O Response Builder conhece apenas o Result.       |
| AI Providers        | Implementações pertencem à infraestrutura.        |
| Tools               | Capacidades pertencem ao Tool Engine.             |

Essas restrições garantem que a construção da resposta permaneça completamente independente da forma como o resultado foi produzido.

---

# Comunicação Permitida

O Response Builder comunica-se exclusivamente por contratos arquiteturais.

```mermaid
flowchart LR

Result

-->

ResponseBuilder

-->

Response
```

Toda comunicação ocorre por meio dos modelos internos do Core.

---

# Comunicação por Contratos

O Response Builder conhece apenas os contratos de entrada e saída definidos pelo Assist Engine.

Exemplos:

```text
Result

Response
```

Essa abordagem garante que qualquer executor compatível com o contrato `Result` possa utilizar o Response Builder sem necessidade de adaptações.

---

# Fluxo Arquitetural

O Response Builder participa exclusivamente do encerramento do processamento interno.

```mermaid
flowchart LR

Executor

-->

Result

-->

ResponseBuilder

-->

Response
```

Após produzir a Response, sua participação é encerrada.

---

# Restrições Arquiteturais

O Response Builder deve obedecer às seguintes restrições.

* Nunca executar regras de negócio.
* Nunca selecionar estratégias.
* Nunca conhecer executores.
* Nunca comunicar-se com infraestrutura.
* Nunca utilizar provedores de IA.
* Nunca executar Tools.
* Nunca modificar o Result recebido.
* Nunca acessar canais de comunicação.

Sua responsabilidade limita-se exclusivamente à construção da Response.

---

# Justificativa Arquitetural

O Response Builder estabelece um contrato único de saída para o Assist Engine.

Ao conhecer exclusivamente os modelos `Result` e `Response`, elimina qualquer acoplamento entre a construção da resposta e os mecanismos responsáveis pela execução da requisição.

Essa decisão garante que novos executores possam ser incorporados ao sistema sem exigir alterações no processo de construção das respostas.

---

# Checklist Arquitetural

Antes de adicionar uma nova dependência ao Response Builder, responda às seguintes perguntas:

* Essa dependência participa da construção da Response?
* Ela pode ser representada por um contrato?
* Ela introduz conhecimento sobre um executor?
* Ela depende da infraestrutura?
* Ela modifica o fluxo arquitetural?

Caso alguma resposta seja positiva para as três últimas perguntas, a dependência não deve ser adicionada.

---

# Considerações Finais

O Response Builder possui deliberadamente o menor conjunto de dependências do Core.

Ao conhecer apenas os contratos de entrada (`Result`) e saída (`Response`), preserva o desacoplamento entre os executores e a construção da resposta, garantindo que todas as estratégias de execução compartilhem o mesmo mecanismo de saída.

Essa abordagem reforça um dos princípios fundamentais do Assist Engine: os executores produzem resultados; somente o Response Builder produz a resposta oficial da arquitetura.
