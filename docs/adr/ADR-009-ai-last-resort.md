# Decisão 009

### Título

Utilizar Inteligência Artificial apenas como último recurso

### Contexto

O objetivo do Assist Engine é oferecer respostas rápidas, previsíveis e com baixo custo computacional sempre que possível.

Grande parte das solicitações pode ser atendida por mecanismos determinísticos, como regras de negócio, consultas estruturadas, templates, buscas locais, pipelines especializados e processamento convencional.

Embora os Modelos de Linguagem (LLMs) sejam extremamente poderosos, sua utilização envolve maior custo, maior latência e respostas probabilísticas, que podem variar entre execuções.

Dessa forma, a IA deve ser utilizada apenas quando os mecanismos tradicionais não forem capazes de produzir uma resposta satisfatória.

### Alternativas consideradas

**1. Utilizar IA em todas as requisições**

Toda solicitação seria enviada diretamente para um modelo de linguagem.

**2. Decisão baseada apenas em regras fixas**

Nunca utilizar IA, limitando o sistema a respostas determinísticas.

**3. Utilizar IA apenas como último recurso**

Priorizar mecanismos determinísticos e recorrer à IA somente quando necessário.

### Decisão

O Assist Engine adotará o princípio de **IA como último recurso**.

O fluxo de decisão deverá sempre priorizar mecanismos determinísticos antes da utilização de um Modelo de Linguagem.

A ordem de prioridade será:

1. Respostas estáticas ou configuradas.
2. Regras de negócio.
3. Templates.
4. Buscas locais e consultas estruturadas.
5. Pipelines especializados.
6. Ferramentas e integrações externas.
7. Inteligência Artificial.

A IA somente será acionada quando as etapas anteriores não forem capazes de atender à solicitação com qualidade suficiente ou quando a natureza da tarefa exigir capacidades de interpretação, geração de linguagem ou raciocínio que não possam ser obtidas por meios determinísticos.

A decisão de utilizar IA deverá ser centralizada na Decision Engine, mantendo esse comportamento consistente em toda a arquitetura.

### Consequências

#### Positivas

✔ Redução significativa dos custos com chamadas a modelos de IA.

✔ Menor latência para a maioria das requisições.

✔ Maior previsibilidade nas respostas.

✔ Melhor aproveitamento de mecanismos determinísticos.

✔ Arquitetura mais eficiente e escalável.

✔ A utilização da IA torna-se uma capacidade complementar, e não a base de funcionamento do sistema.

#### Negativas

✖ A Decision Engine torna-se mais complexa devido à necessidade de avaliar quando a IA realmente é necessária.

✖ Algumas funcionalidades exigirão regras bem definidas para evitar o uso excessivo ou insuficiente da IA.

✖ Novos tipos de requisição podem exigir ajustes periódicos nos critérios de decisão.