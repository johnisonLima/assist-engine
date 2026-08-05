# Decisão 008

## Título

Pipeline composto por Pipeline Steps

## Contexto

O Assist Engine utiliza uma arquitetura baseada em Pipeline para processar requisições de forma sequencial, permitindo que cada etapa agregue comportamento ao fluxo sem acoplamento excessivo.

À medida que novas funcionalidades forem adicionadas (autenticação, autorização, validação, enriquecimento de contexto, cache, observabilidade, rate limiting, auditoria, entre outras), é fundamental que o pipeline permaneça modular, extensível e de fácil manutenção.

Sem regras bem definidas, existe o risco de criar etapas responsáveis por múltiplas tarefas, dependentes umas das outras ou que alterem o fluxo de maneira imprevisível, tornando a arquitetura difícil de evoluir.

## Alternativas consideradas

**1. Pipeline com etapas multifuncionais**

Cada etapa executaria diversas responsabilidades relacionadas.

**2. Pipeline com etapas fortemente acopladas**

Cada etapa dependeria diretamente da execução e implementação da etapa anterior.

**3. Pipeline composto por Pipeline Steps especializados**

Cada etapa executa apenas uma responsabilidade técnica, podendo ser adicionada, removida ou reorganizada sem impactar as demais.

## Decisão

O pipeline da aplicação será composto exclusivamente por **Pipeline Steps**.

Cada Pipeline Step deve obrigatoriamente:

- possuir responsabilidade única;
- ser independente dos demais;
- executar apenas uma tarefa técnica;
- receber a mesma requisição compartilhada entre todas as etapas;
- enriquecer essa requisição adicionando apenas as informações sob sua responsabilidade;
- devolver a mesma instância da requisição enriquecida para a próxima etapa;
- não interromper o fluxo arquitetural, salvo em situações excepcionais, como falhas de autenticação, autorização, validações impeditivas ou erros irrecuperáveis.

Os Pipeline Steps não devem conhecer a implementação dos demais Steps, apenas o contrato do pipeline.

A ordem de execução será definida pela composição do pipeline e não por dependências internas entre os Steps.

## Consequências

#### Positivas

✔ Baixo acoplamento entre as etapas.

✔ Alta coesão, com cada Step possuindo uma única responsabilidade.

✔ Facilidade para adicionar, remover ou reorganizar Steps.

✔ Melhor testabilidade, permitindo testes unitários isolados para cada etapa.

✔ Maior reutilização de Steps em diferentes pipelines.

✔ Arquitetura compatível com os princípios SOLID, especialmente o Single Responsibility Principle (SRP) e o Open/Closed Principle (OCP).

✔ Pipeline previsível, onde cada etapa apenas enriquece a requisição antes de encaminhá-la à próxima.

#### Negativas

✖ Um número maior de Steps pode aumentar a quantidade de classes do projeto.

✖ A definição da ordem correta do pipeline passa a ser responsabilidade da composição arquitetural.

✖ Algumas funcionalidades poderão exigir o compartilhamento de informações na requisição enriquecida, exigindo cuidado na definição do contrato do objeto de contexto.