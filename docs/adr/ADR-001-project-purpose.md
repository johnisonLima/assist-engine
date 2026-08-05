# ADR-0001 — Objetivo do Projeto

**Status:** Accepted

**Data:** Julho de 2026

---

# Contexto

Grande parte dos projetos de assistentes virtuais nasce fortemente acoplada a um modelo de Inteligência Artificial ou a um canal de comunicação específico.

É comum encontrar aplicações cuja lógica de negócio depende diretamente de APIs de IA, tornando difícil substituir provedores, reutilizar componentes ou adicionar novos canais de atendimento.

Além disso, muitas soluções delegam praticamente toda a responsabilidade do sistema ao modelo de linguagem, aumentando custos operacionais, reduzindo previsibilidade e dificultando testes.

Era necessário definir uma arquitetura cujo foco fosse a engenharia de software, utilizando modelos de IA apenas como um dos componentes do sistema.

---

# Decisão

O Assist Engine será desenvolvido como um motor genérico para construção de assistentes inteligentes.

O núcleo da aplicação será completamente independente de:

* canais de comunicação;
* provedores de Inteligência Artificial;
* regras de negócio específicas;
* mecanismos de armazenamento;
* frameworks e bibliotecas.

A Inteligência Artificial será tratada como um serviço especializado de interpretação e geração de linguagem natural, podendo ser utilizada apenas quando realmente necessária.

Toda a lógica de negócio permanecerá sob responsabilidade do Core e dos módulos de negócio da aplicação.

O Assist Engine deverá fornecer uma arquitetura reutilizável, permitindo que diferentes aplicações compartilhem o mesmo núcleo de processamento.

---

# Justificativa

Essa decisão reduz o acoplamento entre os componentes do sistema, aumenta a reutilização do núcleo da aplicação e facilita a evolução tecnológica.

Ao desacoplar a IA do restante da arquitetura, torna-se possível substituir modelos, integrar novos provedores ou até executar partes significativas do fluxo sem qualquer utilização de modelos de linguagem.

Essa abordagem também favorece testes automatizados, manutenção, escalabilidade e redução de custos operacionais relacionados ao consumo de tokens.

---

# Consequências

## Positivas

* Arquitetura independente de fornecedores de IA.
* Facilidade para adicionar novos canais de comunicação.
* Reutilização do Core em diferentes projetos.
* Redução do consumo de tokens.
* Maior previsibilidade do comportamento do sistema.
* Facilidade para testes unitários e de integração.
* Evolução tecnológica com menor impacto na arquitetura.

## Negativas

* Maior esforço inicial de modelagem.
* Número maior de componentes arquiteturais.
* Curva de aprendizado superior à de um chatbot tradicional.
* Necessidade de definir contratos claros entre os módulos.

---

# Alternativas Consideradas

## Construir um chatbot acoplado ao provedor de IA

Essa alternativa permitiria uma implementação inicial mais rápida, porém criaria forte dependência tecnológica, dificultando futuras migrações e reduzindo a reutilização do projeto.

**Decisão:** Rejeitada.

---

## Centralizar toda a lógica na Inteligência Artificial

Delegar decisões de negócio ao modelo de linguagem simplificaria parte do desenvolvimento inicial, porém aumentaria custos, reduziria previsibilidade e dificultaria testes automatizados.

**Decisão:** Rejeitada.

---

## Desenvolver uma arquitetura específica para um único canal

Essa abordagem reduziria a complexidade inicial, mas impediria o reaproveitamento do núcleo em diferentes plataformas de comunicação.

**Decisão:** Rejeitada.

---

# Impacto na Arquitetura

Este ADR estabelece o princípio fundamental do Assist Engine:

> O Core é o elemento central da arquitetura. A Inteligência Artificial, os canais de comunicação, os módulos de negócio e as tecnologias utilizadas são componentes periféricos e substituíveis.

Todas as decisões arquiteturais futuras deverão preservar esse princípio.
