# 5. Matriz Geral de Dependências

Após definir os princípios arquiteturais e os diferentes tipos de dependência, esta seção consolida essas regras em uma matriz de referência.

Seu objetivo é fornecer uma visão rápida das relações permitidas entre todos os componentes do Assist Engine, servindo como consulta durante a implementação, revisão de código e evolução da arquitetura.

A matriz não substitui os documentos individuais dos componentes.

Ela resume, de forma objetiva, quais relações são permitidas pela arquitetura versão 1.0.

---

# 5.1 Legenda

A matriz utiliza a seguinte convenção.

| Símbolo | Significado                                                              |
| ------- | ------------------------------------------------------------------------ |
| ✅       | Dependência direta permitida.                                            |
| 🔒      | Dependência permitida exclusivamente por contrato (abstração/interface). |
| ❌       | Dependência proibida pela arquitetura.                                   |
| —       | Não aplicável (o próprio componente).                                    |

Sempre que existir a possibilidade de utilizar contratos arquiteturais, eles devem ser preferidos em relação às dependências diretas.

---

# 5.2 Matriz Geral

Na matriz abaixo, **as linhas representam o componente consumidor da dependência** e **as colunas representam o componente conhecido**.

| Componente              | Communication | Adapter | Pipeline | Orchestrator | Decision | Rule | Tool |  AI | Business | Response |
| ----------------------- | :-----------: | :-----: | :------: | :----------: | :------: | :--: | :--: | :-: | :------: | :------: |
| **Communication Layer** |       —       |    ✅    |     ❌    |       ❌      |     ❌    |   ❌  |   ❌  |  ❌  |     ❌    |     ❌    |
| **Adapter Layer**       |       ✅       |    —    |     ✅    |       ❌      |     ❌    |   ❌  |   ❌  |  ❌  |     ❌    |    🔒    |
| **Pipeline**            |       ❌       |    ✅    |     —    |      🔒      |     ❌    |   ❌  |   ❌  |  ❌  |     ❌    |     ❌    |
| **Orchestrator**        |       ❌       |    ❌    |    🔒    |       —      |    🔒    |  🔒  |  🔒  |  🔒 |    🔒    |    🔒    |
| **Decision Engine**     |       ❌       |    ❌    |     ❌    |       ❌      |     —    |  🔒  |  🔒  |  🔒 |    🔒    |     ❌    |
| **Rule Engine**         |       ❌       |    ❌    |     ❌    |       ❌      |     ❌    |   —  |   ❌  |  ❌  |     ❌    |    🔒    |
| **Tool Engine**         |       ❌       |    ❌    |     ❌    |       ❌      |     ❌    |   ❌  |   —  |  ❌  |     ❌    |    🔒    |
| **AI Engine**           |       ❌       |    ❌    |     ❌    |       ❌      |     ❌    |   ❌  |   ❌  |  —  |     ❌    |    🔒    |
| **Business Modules**    |       ❌       |    ❌    |     ❌    |       ❌      |     ❌    |   ❌  |   ❌  |  ❌  |     —    |    🔒    |
| **Response Builder**    |       ❌       |    🔒   |     ❌    |       ❌      |     ❌    |   ❌  |   ❌  |  ❌  |     ❌    |     —    |

---

# 5.3 Interpretação da Matriz

A matriz deve ser interpretada sempre do componente da linha para o componente da coluna.

Por exemplo:

```
Pipeline → Orchestrator = 🔒
```

Significa que o Pipeline pode conhecer apenas o contrato do Orchestrator.

Já:

```
Pipeline → Decision Engine = ❌
```

Indica que essa dependência é proibida pela arquitetura.

Da mesma forma:

```
Communication Layer → Adapter Layer = ✅
```

Representa uma dependência direta permitida.

---

# 5.4 Dependências por Contrato

Os componentes marcados com 🔒 devem comunicar-se exclusivamente por contratos definidos pelo Core.

Exemplos:

| Relação                             | Contrato esperado                 |
| ----------------------------------- | --------------------------------- |
| Pipeline → Orchestrator             | `IOrchestrator`                   |
| Orchestrator → Decision Engine      | `IDecisionEngine`                 |
| Orchestrator → Rule Engine          | `IExecutor`                       |
| Orchestrator → Tool Engine          | `IExecutor`                       |
| Orchestrator → AI Engine            | `IExecutor`                       |
| Orchestrator → Business Modules     | `IExecutor` ou `IBusinessModule`* |
| Orchestrator → Response Builder     | `IResponseBuilder`                |
| Rule Engine → Response Builder      | Contrato de `Result`              |
| Tool Engine → Response Builder      | Contrato de `Result`              |
| AI Engine → Response Builder        | Contrato de `Result`              |
| Business Modules → Response Builder | Contrato de `Result`              |
| Response Builder → Adapter Layer    | Contrato de `Response`            |

> **Observação:** Caso todos os executores compartilhem um contrato comum (`IExecutor`), os Business Modules poderão implementá-lo. Caso exista um contrato específico para módulos de negócio, ambos os contratos poderão coexistir sem alterar a arquitetura.

---

# 5.5 Leitura Arquitetural

A matriz evidencia alguns princípios fundamentais do Assist Engine:

* A infraestrutura conhece apenas os componentes imediatamente necessários ao fluxo.
* O Core permanece isolado das implementações concretas.
* Os executores são independentes entre si.
* O Response Builder não conhece nenhum executor.
* Nenhum executor conhece outro executor.
* A comunicação ocorre preferencialmente por contratos.
* Não existem dependências circulares.

Essas características garantem que cada componente permaneça focado em sua responsabilidade, reduzindo o acoplamento e facilitando a evolução da arquitetura.

---

# 5.6 Checklist de Validação

Antes de adicionar uma nova dependência ao sistema, recomenda-se responder às seguintes perguntas:

* A dependência está prevista nesta matriz?
* Existe uma alternativa utilizando contratos?
* Essa relação respeita a direção da arquitetura?
* A nova dependência aumenta o acoplamento do Core?
* Ela introduz uma dependência circular?
* Ela viola a responsabilidade única de algum componente?

Caso alguma dessas perguntas seja respondida negativamente, a implementação deve ser reavaliada antes de prosseguir.

---

# 5.7 Considerações Finais

A Matriz Geral de Dependências representa a visão consolidada das relações permitidas entre os componentes do Assist Engine.

Ela transforma os princípios arquiteturais definidos nas seções anteriores em uma referência prática para implementação, permitindo validar rapidamente se uma nova dependência está alinhada à arquitetura.

Durante o desenvolvimento, esta matriz deve ser consultada sempre que houver dúvida sobre a relação entre dois componentes. Caso uma dependência pretendida não esteja representada nesta matriz, presume-se que ela **não é permitida** até que uma decisão arquitetural formal estabeleça o contrário.
