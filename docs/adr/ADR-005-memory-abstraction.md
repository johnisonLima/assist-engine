# Decisão 005

### Título

Abstração de Provedores de Memória

### Contexto

O Assist Engine pode necessitar armazenar e recuperar informações durante a execução das requisições, como contexto de conversação, memória de curto prazo, memória persistente, histórico de interações ou outros mecanismos de retenção de dados.

Existem diferentes tecnologias capazes de fornecer essas capacidades, incluindo bancos relacionais, bancos NoSQL, bancos vetoriais, sistemas de cache e serviços especializados em memória para IA.

Acoplar o Core a uma tecnologia específica reduziria a flexibilidade da arquitetura e dificultaria a adoção de novas soluções ao longo da evolução do projeto.

### Alternativas consideradas

**1. Utilizar uma única tecnologia de armazenamento**

O Core implementaria diretamente toda a lógica de acesso a uma solução específica de armazenamento.

**2. Criar integrações específicas para cada mecanismo de memória**

Cada funcionalidade acessaria diretamente a tecnologia mais adequada ao seu caso de uso.

**3. Utilizar uma abstração para provedores de memória**

O Core depende apenas de um contrato comum, enquanto diferentes provedores implementam esse contrato utilizando as tecnologias mais adequadas.

### Decisão

O Assist Engine adotará uma **abstração de provedores de memória**.

O Core conhecerá apenas um contrato responsável pelas operações relacionadas à memória, permanecendo independente da tecnologia utilizada para armazenamento.

Cada mecanismo de memória será implementado como um adaptador independente, responsável por traduzir o contrato interno para sua tecnologia correspondente.

Essa abordagem permite utilizar diferentes soluções, como bancos relacionais, bancos NoSQL, bancos vetoriais, sistemas de cache ou outros mecanismos especializados, sem alterar a lógica central da aplicação.

A seleção do provedor de memória será responsabilidade da configuração da aplicação ou da camada de composição, nunca do Core.

### Consequências

#### Positivas

✔ Independência em relação às tecnologias de armazenamento.

✔ Facilidade para adicionar novos mecanismos de memória.

✔ Maior reutilização do Core em diferentes cenários.

✔ Facilidade para criação de implementações de teste.

✔ Redução do acoplamento entre o Core e a infraestrutura.

✔ Alinhamento com a Arquitetura Hexagonal e o Dependency Inversion Principle (DIP).

#### Negativas

✖ Necessidade de manter adaptadores para cada tecnologia suportada.

✖ Algumas funcionalidades específicas de determinadas tecnologias podem não estar disponíveis no contrato comum.

✖ A definição de um contrato suficientemente genérico pode exigir refinamentos conforme novos provedores forem adicionados.
