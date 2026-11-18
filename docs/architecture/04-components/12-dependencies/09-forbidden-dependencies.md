# 9. Dependências Proibidas

Embora o Assist Engine permita diferentes formas de comunicação entre seus componentes, determinadas dependências são explicitamente proibidas pela arquitetura.

Essas restrições existem para preservar a separação de responsabilidades, evitar acoplamentos desnecessários e garantir que a evolução do sistema ocorra sem comprometer sua modularidade.

As dependências descritas nesta seção representam violações da Architecture v1.0 e não devem ser introduzidas durante a implementação.

---

# 9.1 Objetivo

Esta seção estabelece as relações arquiteturais que nunca podem existir entre os componentes do Assist Engine.

Sempre que uma implementação exigir uma das dependências descritas neste documento, a solução deve ser reavaliada, pois provavelmente existe uma violação da arquitetura.

---

# 9.2 Violação entre Infraestrutura e Core

Os componentes da infraestrutura nunca devem conhecer componentes internos do Core além daqueles definidos pela arquitetura.

São proibidas relações como:

```text id="1ujgtt"
Communication Layer
        │
        ▼
Decision Engine
```

```text id="2mn3sl"
Communication Layer
        │
        ▼
Rule Engine
```

```text id="jlwmr6"
Adapter Layer
        │
        ▼
Decision Engine
```

A infraestrutura deve permanecer limitada ao processo de comunicação e adaptação das mensagens.

---

# 9.3 Violação entre Executores

Os executores são completamente independentes entre si.

Nenhum executor pode conhecer outro executor.

São proibidas relações como:

```text id="a63x6d"
Rule Engine
        │
        ▼
Tool Engine
```

```text id="xq4q0k"
Tool Engine
        │
        ▼
AI Engine
```

```text id="b8nbz8"
AI Engine
        │
        ▼
Business Module
```

Essa restrição garante que cada estratégia de execução permaneça isolada das demais.

---

# 9.4 Violação por Implementações Concretas

O Core nunca deve depender diretamente de implementações concretas.

São proibidas relações como:

```text id="0cw17c"
AI Engine
        │
        ▼
OpenAIProvider
```

```text id="jtkj2u"
Tool Engine
        │
        ▼
EmailTool
```

```text id="epycja"
Orchestrator
        │
        ▼
RuleEngine
```

A comunicação deve ocorrer exclusivamente por contratos arquiteturais.

---

# 9.5 Violação entre Engine e Domínio

O Core não possui conhecimento sobre domínios de negócio.

Consequentemente, são proibidas relações como:

```text id="gptkwr"
Decision Engine
        │
        ▼
Agenda Module
```

```text id="wlfc6z"
Pipeline
        │
        ▼
CRM Module
```

```text id="0wkqai"
Response Builder
        │
        ▼
Finance Module
```

Os Business Modules representam extensões da aplicação e permanecem isolados do Engine.

---

# 9.6 Violação da Responsabilidade Única

Nenhum componente pode assumir responsabilidades pertencentes a outro.

Exemplos proibidos:

* Pipeline executando regras de negócio.
* Orchestrator selecionando estratégias.
* Decision Engine executando Tools.
* Rule Engine construindo Responses.
* Response Builder interpretando linguagem natural.

Essas situações caracterizam violação da responsabilidade arquitetural dos componentes.

---

# 9.7 Dependências Circulares

O Assist Engine não admite dependências circulares.

Exemplo:

```text id="6hhyum"
Componente A
        │
        ▼
Componente B
        │
        ▼
Componente A
```

Toda dependência deve possuir direção única.

A existência de ciclos compromete o desacoplamento e dificulta a evolução da arquitetura.

---

# 9.8 Acesso Direto à Infraestrutura

Componentes do Core nunca devem acessar diretamente tecnologias externas.

São proibidas relações como:

```text id="25zjlwm"
Rule Engine
        │
        ▼
Banco de Dados
```

```text id="kv8hn6"
AI Engine
        │
        ▼
SDK HTTP
```

```text id="u8jlwm"
Decision Engine
        │
        ▼
Redis
```

Esses acessos devem ocorrer por meio de contratos e implementações pertencentes às camadas apropriadas.

---

# 9.9 Checklist de Validação

Sempre que uma nova dependência for criada, recomenda-se verificar:

* Existe comunicação direta entre executores?
* Algum componente conhece uma implementação concreta?
* O Core passou a conhecer infraestrutura?
* A infraestrutura passou a conhecer o Core?
* Algum componente assumiu responsabilidade que não lhe pertence?
* Existe dependência circular?
* O relacionamento poderia ser substituído por um contrato?

Caso qualquer resposta seja positiva (exceto a última), a implementação deve ser revisada.

---

# 9.10 Considerações Finais

As dependências proibidas representam limites arquiteturais fundamentais do Assist Engine.

Mais do que impedir determinadas relações, essas restrições preservam os princípios que sustentam a arquitetura: baixo acoplamento, responsabilidade única, independência tecnológica e comunicação por contratos.

Sempre que uma implementação exigir uma dependência proibida, a solução adotada deve ser reconsiderada antes de prosseguir. Na maioria dos casos, a necessidade dessa dependência indica um problema de desenho arquitetural e não uma limitação do Assist Engine.
