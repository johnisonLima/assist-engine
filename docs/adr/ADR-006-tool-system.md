# Decisão 006

### Título

Sistema de Tools

### Contexto

O Assist Engine precisa executar diferentes capacidades técnicas durante o processamento de uma requisição, como consultar informações, acessar serviços externos, manipular arquivos, executar modelos de IA ou interagir com outros sistemas.

Essas capacidades devem ser reutilizáveis, independentes da lógica de negócio e facilmente extensíveis, permitindo que novas funcionalidades sejam adicionadas sem alterações no Core.

Sem um mecanismo padronizado, diferentes partes da aplicação poderiam implementar integrações de maneiras distintas, aumentando o acoplamento e dificultando a manutenção.

### Alternativas consideradas

**1. Implementar integrações diretamente no Core**

Cada funcionalidade técnica seria implementada diretamente nos componentes centrais da aplicação.

**2. Criar integrações específicas para cada fluxo**

Cada pipeline ou módulo implementaria suas próprias integrações conforme a necessidade.

**3. Adotar um Sistema de Tools**

Todas as capacidades técnicas seriam encapsuladas em Tools independentes, acessadas por meio de contratos bem definidos e coordenadas pelo fluxo da aplicação.

### Decisão

O Assist Engine adotará um **Sistema de Tools** como mecanismo padrão para disponibilizar capacidades técnicas ao sistema.

Uma Tool representa uma capacidade reutilizável da plataforma, encapsulando a integração com recursos internos ou externos por meio de uma interface bem definida.

As Tools não devem conter regras de negócio, decisões arquiteturais ou conhecimento sobre o fluxo de execução. Sua responsabilidade é apenas executar a capacidade para a qual foram projetadas e retornar o resultado da operação.

A seleção, composição e utilização das Tools serão responsabilidade da camada de orquestração, preservando a separação entre infraestrutura e lógica da aplicação.

Novas capacidades deverão ser adicionadas por meio da criação de novas Tools, sem necessidade de alterar o Core ou as Tools existentes.

### Consequências

#### Positivas

✔ Padronização das capacidades técnicas do sistema.

✔ Redução do acoplamento entre o Core e integrações externas.

✔ Facilidade para adicionar novas funcionalidades.

✔ Maior reutilização das capacidades em diferentes pipelines.

✔ Facilidade para testes unitários por meio de implementações simuladas.

✔ Arquitetura extensível e alinhada aos princípios SOLID e à Arquitetura Hexagonal.

#### Negativas

✖ A criação de uma Tool para cada capacidade aumenta a quantidade de componentes do projeto.

✖ Algumas operações complexas poderão exigir a composição de múltiplas Tools.

✖ É necessário manter contratos bem definidos para garantir a interoperabilidade entre as Tools e o restante da arquitetura.
