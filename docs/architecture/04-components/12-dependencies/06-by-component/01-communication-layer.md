# Communication Layer

---

# Objetivo

Este documento define as dependências permitidas e proibidas da Communication Layer.

Seu objetivo é preservar o isolamento entre a infraestrutura de comunicação e o restante da arquitetura, garantindo que detalhes específicos dos canais nunca sejam propagados para o Core do Assist Engine.

As regras aqui descritas complementam a documentação do componente, especificando exclusivamente suas relações arquiteturais.

---

# Visão Geral

A Communication Layer representa a fronteira externa do Assist Engine.

Por esse motivo, ela possui o menor conjunto de dependências de toda a arquitetura.

Seu único relacionamento interno ocorre com o Adapter Layer.

```mermaid
flowchart LR

Channel["Canal de Comunicação"]

Communication["Communication Layer"]

Adapter["Adapter Layer"]

Channel --> Communication

Communication --> Adapter
```

---

# Dependências Permitidas

A Communication Layer pode conhecer apenas os seguintes elementos.

| Dependência                   | Tipo           | Justificativa                                 |
| ----------------------------- | -------------- | --------------------------------------------- |
| Adapter Layer                 | Direta         | Encaminhamento das mensagens normalizadas.    |
| Contratos de eventos do canal | Contrato       | Representação dos eventos recebidos do canal. |
| SDKs e APIs do canal          | Infraestrutura | Integração com plataformas externas.          |

Toda dependência adicional deve ser considerada proibida até que uma decisão arquitetural estabeleça o contrário.

---

# Dependências Proibidas

A Communication Layer nunca deve conhecer os seguintes componentes.

| Componente       | Motivo                                                        |
| ---------------- | ------------------------------------------------------------- |
| Pipeline         | Preparação técnica pertence à infraestrutura interna.         |
| Orchestrator     | Coordenação pertence ao Core.                                 |
| Decision Engine  | Tomada de decisão pertence ao Core.                           |
| Rule Engine      | Execução determinística pertence aos executores.              |
| Tool Engine      | Execução de capacidades pertence aos executores.              |
| AI Engine        | Processamento de IA pertence aos executores.                  |
| Business Modules | O Core não possui conhecimento sobre domínios de negócio.     |
| Response Builder | A construção da resposta ocorre após o processamento interno. |

Essa restrição impede que tecnologias específicas de comunicação contaminem o restante da arquitetura.

---

# Comunicação Permitida

A Communication Layer comunica-se exclusivamente com o Adapter Layer.

```mermaid
flowchart LR

Communication

<--> Adapter
```

Nenhuma outra comunicação direta com componentes do Core é permitida.

---

# Comunicação por Contratos

A Communication Layer não conhece implementações internas do Assist Engine.

Sua responsabilidade limita-se ao recebimento e envio de mensagens por meio do Adapter Layer.

Sempre que possível, a comunicação deve ocorrer utilizando contratos arquiteturais definidos pelo Core.

---

# Fluxo Arquitetural

A participação da Communication Layer limita-se ao início e ao fim do ciclo de uma requisição.

```mermaid
flowchart LR

Canal

-->

Communication

-->

Adapter

-. processamento interno .->

Adapter

-->

Communication

-->

Canal
```

Durante todo o processamento interno do Assist Engine, a Communication Layer permanece completamente isolada.

---

# Restrições Arquiteturais

A Communication Layer deve obedecer às seguintes restrições.

* Nunca executar lógica de negócio.
* Nunca interpretar mensagens.
* Nunca selecionar estratégias de execução.
* Nunca conhecer executores.
* Nunca comunicar-se diretamente com o Core.
* Nunca acessar provedores de IA.
* Nunca acessar Tools.
* Nunca acessar Business Modules.

Essas restrições preservam a separação entre infraestrutura e domínio.

---

# Justificativa Arquitetural

A Communication Layer existe exclusivamente para isolar a arquitetura das tecnologias utilizadas pelos canais de comunicação.

Ao limitar suas dependências ao Adapter Layer, o Assist Engine garante que a inclusão de novos canais não produza impactos sobre o Core.

Essa decisão reduz significativamente o acoplamento da arquitetura e mantém o restante do sistema completamente independente das plataformas utilizadas para comunicação.

---

# Checklist Arquitetural

Antes de adicionar qualquer nova dependência à Communication Layer, responda às seguintes perguntas:

* Essa dependência é realmente necessária para comunicação?
* Ela pode ser substituída por um contrato?
* Ela introduz conhecimento sobre o Core?
* Ela aproxima a infraestrutura da lógica de negócio?
* Ela respeita a Architecture v1.0?

Caso alguma resposta seja negativa, a dependência não deve ser adicionada.

---

# Considerações Finais

A Communication Layer possui deliberadamente o menor conjunto de dependências da arquitetura.

Esse isolamento garante que alterações em canais de comunicação permaneçam restritas à infraestrutura, preservando a estabilidade do Core e mantendo o Assist Engine independente das tecnologias utilizadas para interação com o usuário.
