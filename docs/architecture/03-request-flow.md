# Request Flow

**Versão:** 1.0

**Status:** Estável

---

# 1. Objetivo

Este documento descreve o fluxo completo de processamento de uma solicitação dentro do Assist Engine.

Seu propósito é demonstrar como uma mensagem percorre o sistema desde sua entrada em um canal de comunicação até a geração da resposta final.

O fluxo apresentado é independente de linguagem de programação, frameworks ou provedores de Inteligência Artificial, representando exclusivamente o comportamento arquitetural do Assist Engine.

---

# 2. Visão Geral

Toda solicitação segue um fluxo único e previsível.

Cada componente possui responsabilidade exclusiva e executa apenas uma parte do processamento.

Nenhum componente deve assumir responsabilidades pertencentes a outro.

Essa divisão permite que novas funcionalidades sejam incorporadas sem alterar o fluxo principal da arquitetura.

---

# 3. Fluxo Geral

```text
Usuário
    │
    ▼
Communication Layer
    │
    ▼
Adapter Layer
    │
    ▼
Pipeline
    │
    ▼
Orchestrator
    │
    ▼
Decision Engine
    │
    ├──────────────► Rule Engine
    │
    ├──────────────► Tool Engine
    │
    ├──────────────► Business Modules
    │
    ├──────────────► AI Engine
    │
    └──────────────► Human Handoff
    │
    ▼
Response Builder
    │
    ▼
Adapter Layer
    │
    ▼
Communication Layer
    │
    ▼
Usuário
```

Todo atendimento percorre obrigatoriamente esse fluxo.

A estratégia escolhida pelo Decision Engine pode variar, mas a estrutura geral permanece a mesma.

---

# 4. Etapas do Processamento

## 4.1 Recebimento da Mensagem

O processo inicia quando um canal de comunicação recebe um evento.

Esse evento pode representar:

* uma mensagem de texto;
* um clique em botão;
* uma imagem;
* um áudio;
* um documento;
* qualquer outro tipo de interação suportada.

Nesse momento o Assist Engine ainda não conhece o formato da mensagem.

Ela pertence exclusivamente ao canal de origem.

---

## 4.2 Normalização

O Adapter converte a mensagem recebida para um modelo interno padronizado.

A partir desse momento o restante do sistema deixa de conhecer detalhes específicos do canal.

Independentemente de sua origem, todas as mensagens passam a possuir a mesma estrutura lógica.

Esse processo é conhecido como normalização.

---

## 4.3 Pipeline

Após a normalização, a solicitação percorre o Pipeline.

O Pipeline é responsável por executar tarefas técnicas que antecedem o processamento da solicitação.

Entre elas podem estar:

* autenticação;
* identificação da conversa;
* construção do contexto;
* recuperação da memória;
* logging;
* observabilidade;
* validações;
* monitoramento.

Cada etapa possui responsabilidade única e pode ser adicionada, removida ou reorganizada sem alterar o restante do sistema.

Ao término do Pipeline, a solicitação encontra-se preparada para processamento.

---

## 4.4 Orquestração

O Orchestrator recebe a solicitação preparada pelo Pipeline.

Sua função é coordenar o fluxo interno do Assist Engine.

Ele não interpreta mensagens.

Não executa regras de negócio.

Não consulta modelos de IA.

Sua responsabilidade consiste apenas em controlar a sequência de execução dos componentes arquiteturais.

---

## 4.5 Tomada de Decisão

O Decision Engine representa o principal ponto de decisão do sistema.

Seu papel é determinar qual estratégia deverá ser utilizada para atender a solicitação.

Essa decisão considera fatores como:

* tipo da mensagem;
* contexto da conversa;
* estado atual da sessão;
* intenções identificadas;
* políticas de negócio;
* disponibilidade de ferramentas;
* necessidade de utilização de IA.

O Decision Engine nunca executa diretamente nenhuma ação.

Ele apenas escolhe qual componente será responsável pelo atendimento.

---

# 5. Estratégias de Atendimento

Após a tomada de decisão, diferentes caminhos podem ser seguidos.

---

## 5.1 Resposta por Regras

Solicitações simples podem ser respondidas diretamente pelo Rule Engine.

Exemplos:

* menu;
* ajuda;
* comandos conhecidos;
* respostas estáticas.

Nesse cenário nenhum modelo de IA é utilizado.

---

## 5.2 Execução de Ferramentas

Quando uma solicitação exige acesso a recursos externos, o Decision Engine pode delegar o processamento ao Tool Engine.

As Tools representam ações executadas fora do modelo de linguagem.

Exemplos:

* consultar banco de dados;
* chamar APIs;
* enviar e-mails;
* consultar agenda;
* emitir documentos;
* executar cálculos.

O resultado retornado pela Tool pode ser suficiente para construir a resposta ou servir como contexto adicional para outro componente.

---

## 5.3 Execução de Módulos de Negócio

Quando a solicitação pertence a um domínio específico da aplicação, o processamento pode ser delegado a um Business Module.

Esses módulos encapsulam regras de negócio específicas e permanecem completamente independentes do Core do Assist Engine.

---

## 5.4 Utilização de Inteligência Artificial

Quando a interpretação da linguagem natural ou a geração da resposta exigir um modelo de IA, o Decision Engine delega a execução ao AI Engine.

O AI Engine é o único componente autorizado a comunicar-se diretamente com provedores de Inteligência Artificial.

Todo acesso ocorre por meio dos contratos definidos pelo Core.

---

## 5.5 Encaminhamento para Atendimento Humano

Quando definido pelas regras da aplicação, a solicitação poderá ser encaminhada para atendimento humano.

Essa decisão também é responsabilidade do Decision Engine.

---

# 6. Construção da Resposta

Independentemente da estratégia utilizada, todo resultado produzido retorna ao Response Builder.

Esse componente possui duas responsabilidades:

* padronizar a resposta produzida pelos diferentes componentes;
* preparar a resposta para envio ao canal de origem.

Dessa forma, o restante do sistema não precisa conhecer particularidades dos canais de comunicação.

---

# 7. Retorno ao Canal

Após a construção da resposta, o Adapter converte novamente o modelo interno para o formato esperado pelo canal que originou a solicitação.

Somente nesse momento detalhes específicos da plataforma voltam a ser considerados.

O canal então envia a resposta ao usuário, encerrando o ciclo da requisição.

---

# 8. Características do Fluxo

O Request Flow do Assist Engine foi projetado para possuir as seguintes propriedades:

* fluxo único e previsível;
* responsabilidades claramente definidas;
* baixo acoplamento entre componentes;
* alta extensibilidade;
* independência dos canais de comunicação;
* independência dos provedores de IA;
* facilidade para testes;
* facilidade para observabilidade;
* possibilidade de evolução incremental.

Essas características permitem que novos componentes sejam adicionados ao sistema sem alterar o fluxo principal de processamento.

---

# 9. Considerações Arquiteturais

O Request Flow representa um dos pilares do Assist Engine.

Toda solicitação percorre exatamente o mesmo caminho arquitetural, independentemente do canal de origem ou da tecnologia utilizada.

A principal diferença entre dois atendimentos não está no fluxo percorrido, mas na estratégia escolhida pelo Decision Engine.

Esse modelo garante consistência, previsibilidade e desacoplamento, permitindo que o Assist Engine evolua continuamente sem comprometer a arquitetura definida na versão 1.0.
    