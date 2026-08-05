# 2. Princípios Gerais de Dependência

As dependências entre os componentes do Assist Engine são regidas por um conjunto de princípios arquiteturais que garantem a preservação da modularidade, do baixo acoplamento e da independência do Core.

Esses princípios devem orientar toda decisão relacionada à criação de novos componentes, evolução da arquitetura e implementação do sistema.

As regras apresentadas nesta seção possuem caráter normativo e complementam as responsabilidades definidas nos documentos de arquitetura.

---

## 2.1 Dependências seguem a direção da arquitetura

As dependências entre os componentes devem sempre respeitar a direção definida pela arquitetura do Assist Engine.

Nenhum componente pode estabelecer dependências que invertam o fluxo arquitetural ou criem relações circulares entre camadas.

```mermaid
flowchart LR

Communication
    --> Adapter
    --> Pipeline
    --> Orchestrator
    --> Decision
    --> Executors
    --> ResponseBuilder
```

A direção apresentada representa a organização lógica da arquitetura.

Novos componentes devem integrar-se a essa estrutura sem alterar seu sentido.

---

## 2.2 O Core permanece independente da infraestrutura

O Core do Assist Engine nunca deve depender de tecnologias específicas de infraestrutura.

Detalhes relacionados a canais de comunicação, bancos de dados, provedores de IA, bibliotecas externas ou protocolos pertencem exclusivamente às camadas de infraestrutura ou às implementações concretas.

O Core deve conhecer apenas contratos arquiteturais.

Esse princípio garante que novas tecnologias possam ser incorporadas ao sistema sem alterar sua lógica central.

---

## 2.3 Componentes comunicam-se por contratos

Sempre que um componente precisar utilizar outro, a comunicação deve ocorrer por meio de contratos definidos pelo Core.

```text
Orchestrator
        │
        ▼
IDecisionEngine
```

e nunca:

```text
Orchestrator
        │
        ▼
DecisionEngineImpl
```

Essa abordagem reduz o acoplamento entre implementações e permite que componentes sejam substituídos sem impacto sobre o restante da arquitetura.

---

## 2.4 Cada componente conhece apenas o necessário

Um componente deve possuir conhecimento apenas dos elementos indispensáveis para cumprir sua responsabilidade.

Conhecer um componente não significa conhecer sua implementação completa.

Sempre que possível, esse conhecimento deve limitar-se ao contrato arquitetural correspondente.

Quanto menor o conjunto de dependências de um componente, maior sua capacidade de reutilização, teste e evolução.

---

## 2.5 Componentes nunca assumem responsabilidades alheias

Nenhum componente deve executar responsabilidades pertencentes a outro componente da arquitetura.

Quando uma nova necessidade surgir, ela deve ser incorporada ao componente responsável ou motivar a criação de um novo componente, jamais ampliar indevidamente a responsabilidade de um componente existente.

Esse princípio preserva a alta coesão e evita a formação de componentes excessivamente complexos.

---

## 2.6 Dependências circulares são proibidas

O Assist Engine não admite dependências circulares entre componentes.

Situações como:

```text
Componente A
        │
        ▼
Componente B
        │
        ▼
Componente A
```

violam os princípios da arquitetura e aumentam significativamente o acoplamento do sistema.

Toda relação entre componentes deve possuir direção única e claramente definida.

---

## 2.7 Implementações concretas permanecem isoladas

As implementações concretas pertencem às camadas externas da arquitetura.

O Core nunca deve depender diretamente de classes específicas de infraestrutura.

Por exemplo:

```text
AI Engine
        │
        ▼
IAIProvider
```

é permitido.

Entretanto:

```text
AI Engine
        │
        ▼
OpenAIProvider
```

representa um acoplamento indevido entre o Core e uma implementação concreta.

Esse princípio aplica-se igualmente a Tools, Business Modules, canais de comunicação e demais extensões da arquitetura.

---

## 2.8 A direção da comunicação não define dependência

O fluxo de uma requisição não determina, necessariamente, uma dependência arquitetural.

Um componente pode receber informações produzidas por outro sem conhecer sua implementação.

Por exemplo, o Response Builder recebe o resultado produzido por um executor, mas não possui conhecimento sobre qual executor o produziu.

Esse comportamento é possível porque a comunicação ocorre por meio de contratos compartilhados.

Separar claramente comunicação de dependência é fundamental para preservar o desacoplamento do Assist Engine.

---

## 2.9 Novos componentes devem respeitar os princípios existentes

A inclusão de novos componentes não altera os princípios estabelecidos pela arquitetura.

Todo novo componente deve integrar-se às relações já existentes, respeitando:

* a direção das dependências;
* a comunicação por contratos;
* a responsabilidade única;
* a independência do Core;
* a ausência de dependências circulares.

Caso um novo componente exija a quebra de algum desses princípios, sua introdução deve ser reavaliada antes de prosseguir com a implementação.

---

## 2.10 As dependências preservam a arquitetura

As dependências definidas neste documento existem para preservar a estabilidade do Assist Engine durante sua evolução.

Mais do que restringir relações entre componentes, elas estabelecem limites claros que impedem o crescimento desordenado do sistema e mantêm a arquitetura coerente com os princípios definidos desde a versão 1.0.

Toda nova dependência deve ser analisada sob a perspectiva da arquitetura, e não apenas da implementação.

Quando corretamente aplicados, esses princípios permitem que o Assist Engine evolua continuamente sem comprometer sua modularidade, previsibilidade e independência tecnológica.
