# Decisão 002

### Título

Arquitetura Hexagonal

### Contexto

O Assist Engine foi concebido para ser um mecanismo de orquestração reutilizável, extensível e independente de tecnologias específicas. Sua responsabilidade é coordenar o fluxo de execução entre diferentes componentes, como ferramentas, provedores, modelos de IA e módulos de domínio.

Uma arquitetura fortemente acoplada aos frameworks ou às tecnologias externas dificultaria a evolução do projeto, aumentaria o custo de testes e limitaria a substituição de implementações ao longo do tempo.

É necessário que as regras centrais do sistema permaneçam isoladas da infraestrutura, permitindo que novas integrações sejam adicionadas sem impactar o núcleo da aplicação.

### Alternativas consideradas

**1. Arquitetura em Camadas (Layered Architecture)**

Organizar o sistema em camadas tradicionais, como apresentação, serviço e infraestrutura.

**2. Arquitetura orientada ao Framework**

Permitir que o framework defina a organização da aplicação e a comunicação entre seus componentes.

**3. Arquitetura Hexagonal (Ports and Adapters)**

Isolar o Core por meio de portas (contratos) e adaptadores (implementações), permitindo que toda comunicação com o ambiente externo ocorra através de interfaces bem definidas.

### Decisão

O Assist Engine adotará a **Arquitetura Hexagonal (Ports and Adapters)** como padrão arquitetural.

O Core da aplicação conterá apenas as responsabilidades centrais do sistema e dependerá exclusivamente de abstrações.

Toda interação com recursos externos deverá ocorrer por meio de portas (interfaces), enquanto as implementações concretas serão fornecidas por adaptadores.

Entre os componentes que deverão ser implementados como adaptadores estão:

- provedores de IA;
- provedores de memória;
- bancos de dados;
- APIs externas;
- mecanismos de armazenamento;
- sistemas de mensageria;
- ferramentas externas.

Essa separação garante que mudanças em tecnologias ou fornecedores não impactem a lógica central da aplicação.

### Consequências

#### Positivas

✔ Isolamento do Core em relação à infraestrutura.

✔ Baixo acoplamento entre regras de negócio e tecnologias externas.

✔ Facilidade para substituir implementações sem alterar o núcleo da aplicação.

✔ Maior testabilidade por meio de mocks e implementações de teste.

✔ Melhor organização arquitetural e separação de responsabilidades.

✔ Arquitetura preparada para evolução e extensibilidade.

#### Negativas

✖ A quantidade de interfaces e adaptadores aumenta em comparação a arquiteturas mais simples.

✖ Exige maior disciplina para impedir dependências diretas entre o Core e a infraestrutura.

✖ Pode aumentar a complexidade inicial do projeto devido à criação das abstrações necessárias.