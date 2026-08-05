# 11. Antipadrões de Dependência

A arquitetura do Assist Engine foi concebida para manter baixo acoplamento, alta coesão e independência entre seus componentes.

Entretanto, ao longo da evolução do sistema, determinadas decisões de implementação podem comprometer esses princípios e introduzir dependências inadequadas.

Esta seção apresenta os principais antipadrões de dependência que devem ser evitados durante o desenvolvimento.

Os exemplos apresentados não representam apenas más práticas de implementação, mas violações dos princípios arquiteturais definidos para o Assist Engine.

---

# 11.1 Objetivo

O objetivo desta seção é identificar situações que aumentam o acoplamento entre componentes, dificultam a evolução da arquitetura e comprometem sua modularidade.

O reconhecimento desses antipadrões permite corrigi-los antes que se tornem parte da estrutura permanente do sistema.

---

# 11.2 Dependência de Implementações Concretas

Um dos antipadrões mais comuns consiste em depender diretamente de implementações concretas em vez de contratos arquiteturais.

Exemplo:

```text id="s9p8e7"
AI Engine
        │
        ▼
OpenAIProvider
```

A forma correta é:

```text id="m5h2xq"
AI Engine
        │
        ▼
IAIProvider
```

Esse princípio aplica-se igualmente a Tools, Business Modules, Pipeline Steps e demais extensões da arquitetura.

---

# 11.3 Acoplamento entre Executores

Os executores representam estratégias independentes de processamento.

Consequentemente, nunca devem conhecer uns aos outros.

Exemplos de antipadrões:

```text id="q8y4nd"
Rule Engine
        │
        ▼
Tool Engine
```

```text id="v3g7kc"
Tool Engine
        │
        ▼
AI Engine
```

```text id="j1z8mw"
Business Module
        │
        ▼
Rule Engine
```

Sempre que um executor depender de outro, a arquitetura deve ser reavaliada.

---

# 11.4 Violação da Responsabilidade Única

Outro antipadrão recorrente consiste em atribuir responsabilidades pertencentes a outro componente.

Exemplos:

* Pipeline executando regras de negócio.
* Decision Engine executando estratégias.
* Orchestrator tomando decisões.
* Response Builder interpretando linguagem natural.
* AI Engine coordenando o fluxo arquitetural.

Essas situações tornam os componentes mais complexos e enfraquecem a separação de responsabilidades.

---

# 11.5 Dependências Circulares

Dependências circulares comprometem a modularidade da arquitetura e dificultam testes, manutenção e evolução.

Exemplo:

```text id="u2l6fh"
Componente A
        │
        ▼
Componente B
        │
        ▼
Componente A
```

No Assist Engine, toda dependência deve possuir direção única.

---

# 11.6 Contaminação do Core

O Core deve permanecer independente de tecnologias específicas.

São considerados antipadrões:

```text id="n7x4rk"
Orchestrator
        │
        ▼
SDK HTTP
```

```text id="d5q8vl"
Decision Engine
        │
        ▼
Redis
```

```text id="b6w1cm"
Rule Engine
        │
        ▼
Banco de Dados
```

Toda integração tecnológica deve ocorrer por contratos e implementações externas ao Core.

---

# 11.7 Contaminação por Domínio

O Assist Engine é um motor genérico.

Qualquer conhecimento específico de negócio deve permanecer nos Business Modules.

São exemplos de antipadrões:

* Rule Engine contendo regras específicas da aplicação.
* AI Engine conhecendo entidades do domínio.
* Decision Engine tomando decisões baseadas em regras de negócio.
* Pipeline manipulando informações específicas da aplicação.

Esse tipo de dependência reduz significativamente a reutilização do Engine.

---

# 11.8 Componentes Multifuncionais

Um componente que acumula responsabilidades de diferentes naturezas tende a crescer continuamente.

Exemplos:

* Pipeline validando autenticação, executando regras e acessando banco.
* Tool Engine implementando lógica de negócio.
* Business Module construindo Responses.
* Response Builder executando consultas.

Sempre que um componente assumir responsabilidades além de sua função arquitetural, deve-se considerar uma refatoração.

---

# 11.9 Criação Excessiva de Dependências

Adicionar dependências por conveniência de implementação é um dos principais fatores de degradação arquitetural.

Antes de criar uma nova dependência, recomenda-se verificar:

* ela representa uma necessidade arquitetural?
* existe um contrato que possa ser reutilizado?
* o acoplamento realmente é inevitável?
* a responsabilidade está no componente correto?

Nem toda facilidade de implementação resulta em uma boa decisão arquitetural.

---

# 11.10 Checklist de Revisão Arquitetural

Durante revisões de código, recomenda-se verificar:

* Existe dependência de implementação concreta?
* Algum executor conhece outro executor?
* O Core conhece infraestrutura?
* Há dependências circulares?
* Algum componente possui mais de uma responsabilidade?
* Existe conhecimento de domínio dentro do Engine?
* A comunicação ocorre por contratos?
* A nova dependência respeita a matriz arquitetural?

Qualquer resposta positiva para os cinco primeiros itens deve ser tratada como um possível problema arquitetural.

---

# 11.11 Considerações Finais

Os antipadrões apresentados nesta seção representam situações que comprometem a arquitetura do Assist Engine e devem ser evitados durante todo o ciclo de vida do projeto.

Mais do que listar erros comuns, este documento estabelece critérios objetivos para identificar sinais de degradação arquitetural antes que eles se consolidem na implementação.

Ao reconhecer esses antipadrões e corrigi-los precocemente, o Assist Engine preserva seus princípios fundamentais de baixo acoplamento, responsabilidade única, comunicação por contratos e independência tecnológica, garantindo que sua arquitetura permaneça consistente e evolutiva ao longo do tempo.
