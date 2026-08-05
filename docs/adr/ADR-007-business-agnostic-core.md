# Decisão 007

### Título

O Core não possui conhecimento sobre domínios de negócio

### Contexto

O Assist Engine foi concebido para ser um motor de assistência reutilizável, capaz de atender diferentes aplicações e contextos sem depender de um domínio específico.

Ao incorporar regras ou conceitos de negócio diretamente no Core, sua reutilização torna-se limitada, além de aumentar o acoplamento entre a infraestrutura da plataforma e as necessidades de uma aplicação específica.

Para garantir flexibilidade e facilitar a evolução do projeto, é necessário separar claramente a infraestrutura do Assist Engine das implementações de domínio.

### Alternativas consideradas

**1. Incorporar regras de negócio no Core**

O Core conheceria conceitos específicos do domínio da aplicação, implementando comportamentos voltados para um caso de uso específico.

**2. Permitir que o Core conheça parcialmente o domínio**

Algumas abstrações de negócio seriam compartilhadas entre o Core e os módulos de domínio.

**3. Manter o Core completamente agnóstico ao domínio**

O Core fornece apenas a infraestrutura necessária para execução do Assist Engine, enquanto todo conhecimento de negócio permanece em módulos externos.

### Decisão

O Core do Assist Engine **não deve possuir conhecimento sobre qualquer domínio de negócio**.

Sua responsabilidade é fornecer exclusivamente a infraestrutura necessária para o funcionamento do sistema, incluindo componentes como:

- Pipeline;
- Pipeline Steps;
- Decision Engine;
- Tool Engine;
- Agentes;
- Contexto de execução;
- Contratos e interfaces;
- Observabilidade;
- Tratamento de erros;
- Mecanismos de extensão.

Todo conceito relacionado ao domínio da aplicação — como entidades, regras de negócio, políticas, fluxos específicos ou terminologia própria — deve ser implementado em módulos externos que utilizam as capacidades oferecidas pelo Core.

O Core deve depender apenas de abstrações, nunca de implementações de domínio, preservando sua independência e reutilização.

### Consequências

#### Positivas

✔ O Core torna-se reutilizável em diferentes projetos e domínios.

✔ Redução do acoplamento entre infraestrutura e regras de negócio.

✔ Maior facilidade para evolução da plataforma sem impactar aplicações específicas.

✔ Incentiva uma arquitetura modular e extensível.

✔ Facilita a criação de novos módulos de domínio sem alterações no Core.

✔ Alinhamento com os princípios da Clean Architecture e do Dependency Inversion Principle (DIP).

#### Negativas

✖ Exige maior disciplina para impedir que regras de negócio migrem para o Core.

✖ Algumas abstrações podem demandar um esforço inicial maior para permanecerem genéricas.

✖ A separação entre infraestrutura e domínio pode aumentar a quantidade de módulos do projeto.