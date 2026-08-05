# Decisão 003

### Título

FastAPI como framework da aplicação

### Contexto

O Assist Engine necessita expor APIs para integração com aplicações clientes, além de fornecer uma base sólida para orquestração, execução de pipelines, gerenciamento de ferramentas e comunicação com provedores externos.

O framework adotado deve oferecer alto desempenho, tipagem nativa, boa integração com o ecossistema Python e suporte à documentação automática das APIs, reduzindo o esforço de desenvolvimento e manutenção.

### Alternativas consideradas

**1. Flask**

Framework minimalista e amplamente utilizado, porém exige maior quantidade de configurações e bibliotecas adicionais para oferecer funcionalidades presentes em soluções mais modernas.

**2. Django**

Framework completo para aplicações web, porém fornece diversos recursos que não são necessários para um motor de orquestração como o Assist Engine.

**3. FastAPI**

Framework moderno baseado em ASGI, com suporte nativo à tipagem, programação assíncrona, validação automática de dados e geração de documentação OpenAPI.

### Decisão

O Assist Engine adotará o **FastAPI** como framework para exposição de APIs.

O FastAPI será responsável exclusivamente pela camada de entrada da aplicação, realizando o recebimento das requisições, validação dos dados, serialização das respostas e encaminhamento das solicitações ao Core.

As regras de negócio e a lógica de orquestração permanecerão no Core da aplicação, preservando a separação entre infraestrutura e domínio definida pela Arquitetura Hexagonal.

O uso do FastAPI não deve influenciar a organização interna do Core, permitindo sua substituição por outro framework, caso necessário, sem impactos significativos na arquitetura.

### Consequências

#### Positivas

✔ Alto desempenho para processamento de requisições.

✔ Suporte nativo à programação assíncrona.

✔ Validação automática utilizando tipagem Python.

✔ Geração automática da documentação OpenAPI e Swagger.

✔ Excelente integração com o ecossistema moderno de Python.

✔ Mantém o framework restrito à camada de infraestrutura, preservando a independência do Core.

#### Negativas

✖ Dependência da infraestrutura ASGI para aproveitar todos os recursos do framework.

✖ Desenvolvedores precisam compreender o modelo assíncrono quando aplicável.

✖ Mudanças futuras de framework exigirão a implementação de novos adaptadores para a camada de entrada, embora o Core permaneça inalterado.
