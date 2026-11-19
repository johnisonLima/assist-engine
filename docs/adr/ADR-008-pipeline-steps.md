# Decisão 008

## Título

Pipeline composto por PipelineSteps

## Contexto

O Assist Engine utiliza uma arquitetura baseada em Pipeline para processar requisições de forma sequencial, permitindo que cada etapa agregue comportamento ao fluxo sem acoplamento excessivo.

À medida que novas funcionalidades forem adicionadas (autenticação, autorização, validação, enriquecimento de contexto, cache, observabilidade, rate limiting, auditoria, entre outras), é fundamental que o pipeline permaneça modular, extensível e de fácil manutenção.

Sem regras bem definidas, existe o risco de criar etapas responsáveis por múltiplas tarefas, dependentes umas das outras ou que alterem o fluxo de maneira imprevisível, tornando a arquitetura difícil de evoluir.

## Alternativas consideradas

**1. Pipeline com etapas multifuncionais**

Cada etapa executaria diversas responsabilidades relacionadas.

**2. Pipeline com etapas fortemente acopladas**

Cada etapa dependeria diretamente da execução e implementação da etapa anterior.

**3. Pipeline composto por PipelineSteps especializados**

Cada etapa executa apenas uma responsabilidade técnica, podendo ser adicionada, removida ou reorganizada sem impactar as demais.

## Decisão

O pipeline da aplicação será composto exclusivamente por **PipelineSteps**.

Cada PipelineStep deve obrigatoriamente:

- possuir responsabilidade única;
- ser independente dos demais;
- executar apenas uma tarefa técnica;
- receber a mesma requisição compartilhada entre todas as etapas;
- enriquecer essa requisição adicionando apenas as informações sob sua responsabilidade;
- devolver a mesma instância da requisição enriquecida para a próxima etapa;
- não interromper o fluxo arquitetural, salvo em situações excepcionais, como falhas de autenticação, autorização, validações impeditivas ou erros irrecuperáveis.

Os PipelineSteps não devem conhecer a implementação dos demais PipelineSteps, apenas o contrato do pipeline.

A ordem de execução será definida pela composição do pipeline e não por dependências internas entre os Steps.

## Evolução futura: Middleware

`Middleware` é um conceito distinto de `PipelineStep`. Um Middleware poderá ser introduzido futuramente caso exista uma necessidade concreta de interceptar, envolver ou decorar a execução do Pipeline ou de uma etapa, por exemplo, compondo comportamentos antes e depois da execução. Não há uma abstração Middleware independente nesta decisão; PipelineSteps não são aliases de Middleware.

## Consequências

#### Positivas

✔ Baixo acoplamento entre as etapas.

✔ Alta coesão, com cada PipelineStep possuindo uma única responsabilidade.

✔ Facilidade para adicionar, remover ou reorganizar PipelineSteps.

✔ Melhor testabilidade, permitindo testes unitários isolados para cada etapa.

✔ Maior reutilização de PipelineSteps em diferentes pipelines.

✔ Arquitetura compatível com os princípios SOLID, especialmente o Single Responsibility Principle (SRP) e o Open/Closed Principle (OCP).

✔ Pipeline previsível, onde cada etapa apenas enriquece a requisição antes de encaminhá-la à próxima.

#### Negativas

✖ Um número maior de PipelineSteps pode aumentar a quantidade de classes do projeto.

✖ A definição da ordem correta do pipeline passa a ser responsabilidade da composição arquitetural.

✖ Algumas funcionalidades poderão exigir o compartilhamento de informações na requisição enriquecida, exigindo cuidado na definição do contrato do objeto de contexto.
