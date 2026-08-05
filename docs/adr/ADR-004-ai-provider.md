# Decisão 004

### Título

Abstração de Provedores de Inteligência Artificial

### Contexto

O Assist Engine utiliza Modelos de Linguagem (LLMs) para executar tarefas que não podem ser resolvidas por mecanismos determinísticos.

Existem diversos provedores de IA disponíveis no mercado, cada um com APIs, formatos de requisição, capacidades, custos e políticas de utilização diferentes.

Acoplar o Core diretamente a um provedor específico reduziria a flexibilidade da arquitetura, dificultando substituições, testes e a adoção de novos modelos ao longo do tempo.

### Alternativas consideradas

**1. Utilizar um único provedor de IA**

Toda comunicação com modelos de linguagem seria realizada diretamente por meio da API de um fornecedor específico.

**2. Criar integrações específicas para cada caso de uso**

Cada funcionalidade implementaria sua própria integração com o provedor de IA necessário.

**3. Utilizar uma abstração para provedores de IA**

O Core depende apenas de um contrato comum, enquanto cada provedor implementa esse contrato por meio de um adaptador específico.

### Decisão

O Assist Engine adotará uma **abstração de provedores de Inteligência Artificial**.

O Core conhecerá apenas um contrato que representa a capacidade de interação com modelos de linguagem, permanecendo independente das APIs e características de qualquer fornecedor.

Cada provedor será implementado como um adaptador independente, responsável por traduzir o contrato interno para a API correspondente.

Essa abordagem permite integrar diferentes provedores, como OpenAI, Anthropic, Google, Azure OpenAI, Ollama ou modelos futuros, sem alterações na lógica central da aplicação.

A seleção do provedor a ser utilizado será responsabilidade da camada de configuração ou da lógica de orquestração, nunca do Core.

### Consequências

#### Positivas

✔ Independência em relação a fornecedores específicos.

✔ Facilidade para adicionar novos provedores de IA.

✔ Maior testabilidade por meio de implementações simuladas (mocks).

✔ Redução do acoplamento entre o Core e APIs externas.

✔ Flexibilidade para selecionar provedores conforme custo, desempenho ou capacidade.

✔ Alinhamento com a Arquitetura Hexagonal e o Dependency Inversion Principle (DIP).

#### Negativas

✖ Necessidade de manter adaptadores para cada provedor suportado.

✖ Recursos exclusivos de determinados provedores podem exigir extensões no contrato comum.

✖ A abstração pode não expor imediatamente funcionalidades muito específicas de um fornecedor.
