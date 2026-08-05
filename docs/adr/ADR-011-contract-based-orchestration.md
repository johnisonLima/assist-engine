# Decisão 011

### Título

Orquestração baseada em contratos

### Contexto

O Orchestrator é responsável por coordenar o fluxo de execução do Assist Engine, determinando quais componentes participarão do processamento de cada requisição e como eles serão utilizados.

Caso o Orchestrator conheça implementações concretas, ele se tornará fortemente acoplado aos componentes da aplicação, dificultando substituições, testes, evolução da arquitetura e a introdução de novas funcionalidades.

Para preservar a modularidade do sistema, o Orchestrator deve depender apenas de contratos bem definidos, permitindo que diferentes implementações sejam utilizadas sem alterar sua lógica de coordenação.

### Alternativas consideradas

**1. Coordenar utilizando implementações concretas**

O Orchestrator instancia ou referencia diretamente classes concretas para executar suas responsabilidades.

**2. Utilizar uma abordagem híbrida**

Alguns componentes são acessados por contratos, enquanto outros são utilizados diretamente por suas implementações.

**3. Coordenar exclusivamente por contratos**

O Orchestrator depende apenas de interfaces e contratos, delegando a resolução das implementações ao mecanismo de composição da aplicação.

### Decisão

O Assist Engine adotará uma **orquestração baseada em contratos**.

O Orchestrator conhecerá exclusivamente contratos que representem as capacidades necessárias para coordenar o fluxo de execução da aplicação.

O Orchestrator não deve:

* depender de implementações concretas;
* instanciar componentes diretamente;
* conhecer detalhes de infraestrutura;
* tomar decisões baseadas em tipos concretos.

A resolução das implementações será responsabilidade da camada de composição da aplicação, normalmente realizada por meio de um contêiner de injeção de dependências.

Esse princípio aplica-se a todos os componentes coordenados pelo Orchestrator, incluindo Pipeline Steps, Tools, Providers, Engines, Agentes e quaisquer futuras extensões da plataforma.

### Consequências

#### Positivas

✔ Redução do acoplamento entre o Orchestrator e os componentes do sistema.

✔ Facilidade para substituir implementações sem modificar a lógica de orquestração.

✔ Maior testabilidade por meio de mocks e implementações de teste.

✔ Arquitetura mais modular e extensível.

✔ Alinhamento com o Dependency Inversion Principle (DIP).

✔ Facilidade para incorporar novos componentes ao sistema sem alterações no Orchestrator.

#### Negativas

✖ Exige contratos claros e estáveis entre os componentes.

✖ A configuração da composição da aplicação torna-se parte importante da arquitetura.

✖ A identificação da implementação concreta utilizada pode exigir apoio das ferramentas de diagnóstico durante a execução.
