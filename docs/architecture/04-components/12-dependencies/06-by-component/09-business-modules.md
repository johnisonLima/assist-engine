# Business Modules

---

# Objetivo

Este documento define as dependências permitidas e proibidas dos Busiuness Modules.

Seu objetivo é garantir que os módulos de negócio permaneçam completamente isolados do Core do Assist Engine, preservando a independência entre a arquitetura do Engine e os domínios específicos de cada aplicação.

As regras aqui descritas complementam a documentação do componente, especificando exclusivamente seus relacionamentos arquiteturais.

---

# Visão Geral

Os Business Modules representam os domínios de negócio das aplicações construídas sobre o Assist Engine.

Embora façam parte do fluxo de execução, pertencem à aplicação e não ao Core.

```mermaid
flowchart LR

Orchestrator

-->

BusinessModule

-->

Result
```

Para o Assist Engine, todos os módulos são vistos apenas como implementações de contratos arquiteturais.

---

# Dependências Permitidas

Os Business Modules podem conhecer apenas os seguintes elementos.

| Dependência                                     | Tipo     | Justificativa                                                |
| ----------------------------------------------- | -------- | ------------------------------------------------------------ |
| Contrato do Executor                            | Contrato | Implementação da estratégia de execução.                     |
| Contrato do Business Module (`IBusinessModule`) | Contrato | Representação arquitetural do domínio.                       |
| Modelos internos (Request, Context e Result)    | Contrato | Comunicação com o Core.                                      |
| Componentes pertencentes ao próprio domínio     | Direta   | Implementação da lógica de negócio.                          |
| Infraestrutura específica da aplicação          | Direta   | Persistência, integrações e recursos necessários ao domínio. |

Toda dependência deve permanecer restrita ao domínio representado pelo módulo.

---

# Dependências Proibidas

Os Business Modules nunca devem conhecer diretamente:

| Componente              | Motivo                                               |
| ----------------------- | ---------------------------------------------------- |
| Communication Layer     | Infraestrutura de comunicação pertence ao Engine.    |
| Adapter Layer           | Conversão de formatos pertence ao Engine.            |
| Pipeline                | Preparação da requisição pertence ao Engine.         |
| Orchestrator            | O fluxo é coordenado externamente.                   |
| Decision Engine         | A estratégia já foi selecionada.                     |
| Rule Engine             | Executores permanecem independentes.                 |
| Tool Engine             | Executores permanecem independentes.                 |
| AI Engine               | Executores permanecem independentes.                 |
| Response Builder        | O módulo produz apenas um Result.                    |
| Outros Business Modules | Os domínios devem permanecer independentes entre si. |

Essas restrições preservam o isolamento entre os domínios da aplicação e evitam acoplamento entre módulos.

---

# Comunicação Permitida

Os Business Modules comunicam-se exclusivamente com o Core por contratos arquiteturais.

```mermaid
flowchart LR

IExecutor

-->

IBusinessModule

-->

Result
```

Toda comunicação com outros elementos da aplicação deve ocorrer por contratos definidos pelo próprio domínio.

---

# Comunicação por Contratos

Os Business Modules comunicam-se com o Assist Engine apenas por abstrações definidas pelo Core.

Exemplos:

```text
IExecutor

IBusinessModule

Request

Result
```

Internamente, cada domínio pode definir seus próprios contratos, desde que permaneçam isolados do Core.

---

# Fluxo Arquitetural

Os Business Modules participam apenas da execução da estratégia selecionada.

```mermaid
flowchart LR

Decision

-->

BusinessModule

-->

Result
```

Após produzir o resultado, sua participação é encerrada.

---

# Restrições Arquiteturais

Os Business Modules devem obedecer às seguintes restrições.

* Nunca coordenar o fluxo arquitetural.
* Nunca selecionar estratégias.
* Nunca conhecer outros executores.
* Nunca construir respostas.
* Nunca acessar diretamente canais de comunicação.
* Nunca depender do Core além dos contratos definidos.
* Nunca estabelecer dependências entre domínios de negócio.

Sua responsabilidade limita-se exclusivamente à implementação do domínio representado pelo módulo.

---

# Justificativa Arquitetural

Os Business Modules representam a principal extensão funcional do Assist Engine.

Ao permanecerem completamente isolados do Core, permitem que o mesmo Engine seja reutilizado em aplicações de naturezas completamente diferentes.

Essa decisão reforça um dos princípios fundamentais da arquitetura:

> **O Core não possui conhecimento sobre domínios de negócio.**

Ao mesmo tempo, garante que os domínios permaneçam independentes entre si, favorecendo modularidade, reutilização e evolução incremental.

---

# Checklist Arquitetural

Antes de adicionar uma nova dependência a um Business Module, responda às seguintes perguntas:

* Essa dependência pertence ao domínio de negócio?
* Ela é necessária para implementar um caso de uso?
* Ela depende do Core além dos contratos definidos?
* Ela estabelece comunicação com outro domínio?
* Ela introduz conhecimento sobre a infraestrutura do Engine?

Caso alguma resposta seja positiva para as três últimas perguntas, a dependência não deve ser adicionada.

---

# Considerações Finais

Os Business Modules constituem a fronteira entre o Assist Engine e as aplicações construídas sobre ele.

Ao restringir suas dependências ao próprio domínio e aos contratos definidos pelo Core, preservam a independência entre a plataforma e as regras de negócio.

Essa separação garante que o Assist Engine permaneça um motor genérico para assistentes inteligentes, enquanto cada aplicação evolui de forma autônoma, implementando apenas os domínios necessários ao seu contexto.
