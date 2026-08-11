# ADR-012 — Contexto como Contexto de Execução

* **Status:** Accepted
* **Data:** 2026-08-11

## Contexto

O Assist Engine necessita de um conceito capaz de representar o contexto no qual uma operação do Core é executada.

O termo `Context` pode facilmente ser interpretado como o histórico de uma conversa, especialmente em sistemas baseados em inteligência artificial conversacional. Entretanto, histórico conversacional e contexto de execução representam responsabilidades diferentes.

A memória conversacional é responsável por armazenar ou recuperar informações de interações anteriores. O contexto de execução, por outro lado, representa as informações relevantes para o processamento da operação atual.

Manter esses conceitos separados é importante porque componentes futuros, como Memory, Tools, RAG e Pipeline, poderão fornecer informações para uma execução sem que o `Context` se torne responsável por armazenar essas informações de forma persistente.

## Decisão

O `Context` do Assist Engine representa o **contexto de execução de uma operação do Core** e não é responsável por armazenar ou persistir a memória conversacional.

O `Context` poderá ser enriquecido ao longo da evolução do sistema com informações necessárias para a execução atual, conforme necessidades concretas forem identificadas nas próximas Sprints.

A memória conversacional permanece como uma responsabilidade independente. Quando o sistema de Memory for implementado, poderá recuperar informações relevantes e disponibilizá-las para a execução, mas Memory e Context permanecerão conceitualmente distintos.

A implementação inicial do `Context` é intencionalmente vazia, pois o Core ainda não necessita de informações adicionais para sua execução.

A relação conceitual é:

```text
Memory
   │
   │ recupera informações relevantes
   ▼
Context
   │
   │ fornece o contexto da execução
   ▼
Orchestrator
   │
   ▼
Response
```

Essa decisão não define antecipadamente a estrutura interna definitiva do `Context`. Seus atributos e responsabilidades poderão evoluir conforme novas capacidades forem incorporadas ao sistema.

## Consequências

### Positivas

* Mantém memória conversacional e contexto de execução como responsabilidades distintas.
* Evita transformar o `Context` em um mecanismo genérico de armazenamento do histórico da conversa.
* Permite que Memory, Tools, RAG e outros componentes evoluam de forma independente.
* Estabelece um ponto conceitual para informações necessárias durante uma execução do Core.
* Evita definir prematuramente a estrutura interna do `Context`.

### Negativas

* A distinção entre Context e Memory deverá ser preservada durante a evolução do sistema.
* A estrutura definitiva do `Context` não pode ser completamente definida antecipadamente.
* Futuras integrações poderão exigir decisões específicas sobre quais informações pertencem ao `Context` e quais pertencem a outros componentes.

## Alternativas Consideradas

### Contexto como memória conversacional

O `Context` poderia representar diretamente o histórico da conversa, contendo mensagens anteriores e outras informações persistentes relacionadas à conversação.

Essa abordagem foi rejeitada porque acoplaria o contexto de execução à responsabilidade de memória e faria o Core depender de uma representação específica do histórico conversacional.

### Contexto como recipiente genérico

O `Context` poderia ser implementado como uma estrutura genérica capaz de armazenar qualquer informação fornecida pelos diferentes componentes do sistema.

Essa abordagem foi rejeitada porque poderia transformar o `Context` em um recipiente de dados sem responsabilidades claras, enfraquecendo os contratos e a separação de responsabilidades definidos pela arquitetura.

## Decisões Relacionadas

* **ADR-011 — Contract-Based Orchestration**
* **Memory Provider** — decisão futura sobre memória conversacional
* **Pipeline** — decisão futura sobre etapas de execução e propagação do contexto
* **RAG** — decisão futura sobre conhecimento recuperado externamente
* **Tool System** — decisão futura sobre contexto de execução de ferramentas
