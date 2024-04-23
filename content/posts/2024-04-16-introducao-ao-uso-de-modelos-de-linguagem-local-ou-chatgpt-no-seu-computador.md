---
author:
  name: "Valdecir Carvalho"
date: 2024-04-23
linktitle: ChatGPT no seu Computador - Introdução ao Uso de LLMs locais
featured: true
type:
- post
- posts
title: ChatGPT no seu Computador - Introdução ao Uso de LLMs locais
series:
- AI
- LLM
- Tutorial
- Iniciante
---


![Screenshot Site LM Studio](/img/chatgpt-local.webp)

Olá! Neste post, vou fazer uma introdução ao uso de LLM - Large Language Model / Modelo de Linguagem de Grande Escala que podem ser executados localmente no seu computador, ou para simplificar, como rodar o ChatGPT no seu computador e totalmente grátis.


## Introdução ao uso de LLMs localmente

Os Modelos de Linguagem de Grande Escala (LLMs), como GPT (Generative Pre-trained Transformer) e BERT (Bidirectional Encoder Representations from Transformers), são tipos de inteligência artificial projetados para entender e gerar texto de maneira coerente e contextual. Esses modelos são treinados em vastas quantidades de texto e podem realizar uma variedade de tarefas linguísticas.

Os modelos mais populares incluem o GPT-3 da OpenAI (o famoso ChatGPT), Gemini do Google, Copilot da Microsoft e Claude da Anthropic. Embora muitos LLMs estejam disponíveis como serviços na nuvem, também é possível executá-los localmente em seu computador.

## Mas o que são LLMs?

O termo LLM, que significa Modelo de Linguagem de Grande Escala ou Large Language Model em Inglês, é uma tecnologia avançada no campo da inteligência artificial que se especializa em compreender e gerar texto de forma que se assemelha à maneira como os humanos se comunicam. São treinados em imensos volumes de dados textuais, como livros, websites e bases de dados. Imagine um bibliotecário que leu milhões de livros e é capaz de conversar sobre quase qualquer assunto, responder perguntas ou até mesmo criar histórias novas; essa é a essência de um LLM. Ele é treinado com vastas quantidades de dados textuais para aprender padrões de linguagem, o que lhe permite realizar uma variedade de tarefas linguísticas complexas. _(Microsoft Copilot)_

Você pode pensar em um LLM como um assistente virtual muito sofisticado que não apenas entende o que você diz ou escreve, mas também pode fornecer informações, criar conteúdo, traduzir idiomas e ajudar na aprendizagem, tudo isso com uma compreensão profunda do contexto e nuances da linguagem. É como ter um interlocutor inteligente ao seu lado, sempre pronto para ajudar com suas necessidades de comunicação e informação. _(Microsoft Copilot)_

Para o público geral, o impacto dos LLMs é significativo porque eles facilitam a interação mais natural e intuitiva com a tecnologia. Isso não apenas torna a tecnologia mais acessível para todos, mas também abre novas possibilidades para automação e assistência em setores como educação, atendimento ao cliente, e entretenimento. Em resumo, LLMs são como motores inteligentes que compreendem e produzem linguagem, ajudando a tornar as máquinas mais úteis e compreensíveis para os humanos. _(ChatGPT)_

## Executar LLMs Localmente vs. na Nuvem

Executar Modelos de Linguagem de Grande Escala (LLMs) **localmente** e em **serviços baseados na nuvem** apresentam vantagens e desvantagens distintas como **Velocidade de Processamento**, **Privacidade de Informações** e principalmente o **Uso Pretendido** além do **Custo** envolvido em ambos os cenários.

### Principais Vantagens de Executar Localmente

- **Privacidade**: Ao executar LLMs localmente, seus dados e consultas não são enviados para servidores externos, garantindo uma camada adicional de privacidade.
- **Controle**: Você tem controle total sobre o modelo, permitindo ajustes nos parâmetros, fine-tuning e personalização conforme necessário.
- **Custo**: Depois do investimento inicial em hardware, como computadores e GPUs adequadas, os custos operacionais são menores ou praticamente inexistentes em comparação com os custos recorrentes de serviços baseados em assinatura.

### Principais Desvantagens de Executar Localmente

- **Requisitos de Hardware**: A necessidade de hardware potente, especialmente GPUs de alta capacidade, pode representar um investimento substancial e ser inacessível para muitos.
- **Manutenção**: Você é responsável por atualizar, otimizar e solucionar problemas com os modelos e software.
- **Recursos Limitados**: Os modelos de código aberto geralmente têm recursos menores que os modelos proprietários usados por serviços na nuvem.


### Principais Vantagens de Serviços na Nuvem

- **Facilidade de uso**: Os serviços na nuvem são fáceis de usar e integrar com outras aplicações, graças à disponibilidade de APIs.
- **Acesso a modelos mais recentes e avançados**: Proporcionam acesso a modelos de linguagem de última geração sem a necessidade de hardware especializado.
- **Custos iniciais menores**: Não exigem grandes investimentos iniciais em hardware, reduzindo o custo inicial de implementação.

### Principais Desvantagens de Serviços na Nuvem

- **Dependência de conexão à internet**: Requerem uma conexão de internet estável para funcionar.
- **Preocupações com a privacidade**: O envio de dados para servidores externos pode suscitar questões de segurança e privacidade dos dados.
- **Custos**: Mesmo podendo utilizar a maioria dos serviços sem custo algum, você eventuralmente irá acabar sentindo a necessidade de assinar um ou mais serviços para usar toda sua capacidade ou funcionalidades, ou ainda consumir uma API e os custos podem começar a se acumular.

## Softwares para Executar LLMs Localmente

A seguir vou apresentar brevemente algumas opções de LLMs locais, que são simples de serem instaladas e após alguma configuração, podem ser executadas satisfatoriamente em um computador não tão parrudo.

### LM Studio - [https://lmstudio.ai/](https://lmstudio.ai/)
![Screenshot Site LM Studio](/img/lmstudio-site-screenshot.png)

LM Studio é uma plataforma que possibilita o uso local de modelos de linguagem avançados, com suporte para várias arquiteturas de modelos. Essa ferramenta é ideal para desenvolvedores e pesquisadores que necessitam de um controle mais apurado sobre os modelos e onde a privacidade dos dados é uma preocupação crucial. Ela permite fácil integração com diferentes frameworks de IA e pode ser adaptada para usos específicos.

### Ollama - [https://ollama.com/](https://ollama.com/)
![Screenshot Site LM Studio](/img/ollama-site-screenshot.png)

Ollama é outra solução robusta para executar LLMs localmente. Este sistema se destaca por sua flexibilidade em termos de escalabilidade e pela capacidade de suportar diferentes tipos de hardware, incluindo configurações sem GPU. Ollama é adequado para ambientes onde a privacidade dos dados e a necessidade de uma implementação local são prioritárias.

### JanAI - [https://jan.ai/](https://jan.ai/)
![Screenshot Site LM Studio](/img/janai-site-screenshot.png)

JanAI é uma ferramenta open-source projetada para executar modelos de linguagem de grande escala (LLMs) completamente offline. Suportando uma ampla gama de hardware, de PCs individuais a clusters com múltiplas GPUs, JanAI é particularmente otimizado para dispositivos com GPUs NVIDIA e processadores Apple M-series.  é altamente personalizável através de extensões, permitindo ajustes finos e adaptações para atender a necessidades específicas de pesquisa ou desenvolvimento. Esta plataforma é uma escolha robusta para aqueles que necessitam de controle total sobre a operação e segurança dos modelos de linguagem que utilizam.

## Conclusão

Executar LLMs localmente oferece benefícios significativos em termos de liberdade, privacidade e controle, mas pode exigir um investimento inicial em termos de hardware. Por outro lado, os serviços em nuvem oferecem maior conveniência e acesso a tecnologias de ponta, embora possam levantar preocupações quanto à privacidade dos dados. A escolha entre local e nuvem dependerá das necessidades específicas de cada usuário e da sensibilidade de suas informações.

Nos próximos posts, irei mostrar como instalar e fazer a configuração de cada uma das ferramentas acima.

Até o próximo post!