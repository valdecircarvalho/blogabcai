---
author:
  name: "Valdecir Carvalho"
date: 2024-03-13
linktitle: ola-mundo-da-ia
featured: true
type:
- post
- posts
title: Os 15 principais termos do LLM que você precisa saber em 2024
summary: Neste post, exploraremos os 15 principais termos relacionados a LLMs. Cada termo será detalhado com definições claras e exemplos práticos para ajudar você a entender melhor como essas tecnologias funcionam e como são aplicadas no mundo real.
series:
- AI
- LLM
- GenAI
- Iniciante
---

## Introdução

Os Modelos de Linguagem de Grande Escala (Large Language Models - LLMs) estão moldando o futuro da inteligência artificial e transformando a maneira como interagimos com a tecnologia. As LLMs desempenham um papel crucial na geração e compreensão de texto em diversas aplicações. 

Compreender os principais termos e conceitos associados a esses modelos é essencial para aproveitar ao máximo seu potencial e para se manter atualizado com as tendências emergentes em IA.

Neste post, exploraremos os 15 principais termos relacionados a LLMs. Cada termo será detalhado com definições claras e exemplos práticos para ajudar você a entender melhor como essas tecnologias funcionam e como são aplicadas no mundo real.

## Transformers
**Definição**: Transformers são uma arquitetura de processamento de linguagem que analisa as relações entre palavras em um texto para entender e gerar linguagem de forma mais eficaz.

**Detalhamento**: A arquitetura Transformer utiliza mecanismos de atenção para identificar a importância de cada palavra em relação às outras, permitindo uma compreensão mais profunda do contexto. Esse modelo é fundamental para o funcionamento de muitos LLMs modernos.

**Exemplo Prático**: O ChatGPT se utiliza a arquitetura Transformer para gerar respostas coerentes e contextualmente apropriadas em aplicações como chatbots e assistentes virtuais.

## Tokens
**Definição**: Tokens são as unidades básicas de texto que um LLM processa, como palavras, subpalavras ou caracteres.

**Detalhamento**: A tokenização divide o texto em partes menores que podem ser facilmente processadas pelo modelo. Isso ajuda na análise e geração de texto, permitindo que o modelo compreenda e trabalhe com diferentes segmentos do texto.

**Exemplo Prático**: Em um sistema de processamento de linguagem natural para análise de sentimentos, o texto é **tokenizado** para que o modelo possa analisar cada palavra ou subpalavra separadamente e entender o sentimento expresso. 

## Chunking
**Definição**: Chunking é o processo de dividir o texto em segmentos menores e gerenciáveis para facilitar a análise por um LLM.

**Detalhamento**: Semelhante ao agrupamento de palavras em frases, o chunking ajuda a organizar o texto em partes que podem ser processadas mais eficientemente, melhorando a análise e a geração de texto.

**Exemplo Prático**: Em um sistema de tradução automática, o chunking pode ser usado para dividir o texto em frases ou blocos menores, facilitando a tradução precisa e fluente de um idioma para outro.

## Indexação (Indexing)
**Definição**: Indexação envolve criar um catálogo de dados para permitir a recuperação eficiente de informações específicas em grandes conjuntos de dados.

**Detalhamento**: A indexação é essencial para organizar e acessar rapidamente informações relevantes em grandes bases de dados, melhorando a eficiência dos processos de busca e recuperação.

**Exemplo Prático**: Motores de busca como o Google utilizam indexação para catalogar páginas da web, permitindo que os usuários encontrem rapidamente informações relevantes ao pesquisar por palavras-chave.

## Incorporação (Embeddings)
**Definição**: Embeddings são representações numéricas de palavras ou frases que permitem a um LLM compreender suas relações e significados.

**Detalhamento**: Os embeddings capturam a essência semântica das palavras e são usados para medir similaridades e diferenças entre elas, facilitando a compreensão e a geração de texto.

**Exemplo Prático**: Em um sistema de recomendação de filmes, embeddings podem ser usados para comparar a descrição de um filme com as preferências de um usuário, ajudando a sugerir filmes semelhantes.

## Pesquisa Vetorial (Vector Search)
**Definição**: Pesquisa vetorial envolve encontrar informações semelhantes em grandes conjuntos de dados utilizando embeddings para comparar vetores de características.

**Detalhamento**: Essa técnica é usada para localizar dados relevantes com base em suas representações vetoriais, tornando a busca por informações mais eficiente e precisa.

**Exemplo Prático**: Em um sistema de recuperação de documentos, a pesquisa vetorial pode ser usada para encontrar artigos ou pesquisas que sejam semanticamente semelhantes a uma consulta do usuário.

## Banco de Dados de Vetores (Vector Database)
**Definição**: Um banco de dados de vetores armazena representações numéricas (embeddings) de dados para permitir uma pesquisa vetorial eficiente.

**Detalhamento**: Esses bancos de dados são otimizados para armazenar e recuperar vetores rapidamente, facilitando a busca e análise de grandes volumes de dados.

**Exemplo Prático**: Plataformas de busca de imagens como o Google Imagens utilizam bancos de dados de vetores para armazenar representações de imagens, permitindo a busca por imagens semelhantes.

## Inteligência Geral Artificial (Artificial General Intelligence - AGI)
**Definição**: AGI é o objetivo de criar máquinas que possam pensar e aprender de maneira similar aos humanos, com uma compreensão geral e adaptabilidade.

**Detalhamento**: Enquanto os LLMs atuais são especialistas em tarefas específicas, a AGI visa desenvolver sistemas com habilidades gerais de aprendizado e resolução de problemas que se aproximem da inteligência humana.

**Exemplo Prático**: Atualmente, a AGI ainda é um conceito teórico, mas os avanços em LLMs são passos importantes para alcançar essa meta. A pesquisa em AGI busca criar sistemas que possam realizar uma ampla gama de tarefas com flexibilidade e compreensão semelhantes às capacidades humanas.

## Agente LLM (LLM Agents)
**Definição**: Um agente LLM é um modelo treinado para executar uma tarefa específica, como gerar conteúdo ou responder perguntas em um domínio específico.

**Detalhamento**: Esses agentes são adaptados para lidar com requisitos particulares, melhorando o desempenho e a relevância das respostas ou conteúdos gerados.

**Exemplo Prático**: Um assistente virtual especializado em suporte técnico pode ser um agente LLM treinado para responder a perguntas específicas sobre produtos e serviços, fornecendo suporte personalizado e eficiente.

## Mixture of Experts (MoE)
**Definição**: MoE é uma técnica que utiliza múltiplos modelos especializados menores para melhorar o desempenho em tarefas específicas.

**Detalhamento**: Em vez de usar um único modelo grande, o MoE combina modelos menores especializados em diferentes aspectos, permitindo uma abordagem mais eficiente e eficaz para tarefas complexas.

**Exemplo Prático**: Em um sistema de recomendação, o MoE pode usar especialistas em diferentes categorias de produtos para fornecer recomendações mais precisas e personalizadas para os usuários.

## Shot Learning
**Definição**: Shot learning refere-se à quantidade de exemplos necessários para que um LLM aprenda uma nova tarefa.

**Detalhamento**: Essa técnica mede a eficiência do modelo em aprender a partir de exemplos limitados, impactando a forma como o modelo é treinado e ajustado para novas tarefas.

**Exemplo Prático**: Em um sistema de reconhecimento de imagens, o shot learning pode permitir que o modelo aprenda a identificar novos tipos de objetos com apenas alguns exemplos, facilitando a adaptação a novas categorias.

>> ### Zero-Shot
**Definição**: Zero-shot learning é a capacidade de um LLM realizar uma tarefa sem ter sido treinado especificamente para ela, baseando-se apenas no conhecimento pré-existente.

**Detalhamento**: Essa abordagem permite que o modelo generalize e aplique seu conhecimento para novas tarefas sem a necessidade de exemplos específicos durante o treinamento.

**Exemplo Prático**: Um modelo de tradução automática pode usar zero-shot learning para traduzir um idioma pouco comum para o qual não há muitos exemplos de treinamento, baseando-se em sua compreensão geral de linguagens.

>> ### One-Shot
**Definição**: One-shot learning é o processo de treinar um LLM com apenas um exemplo para realizar uma nova tarefa.

**Detalhamento**: Essa técnica é útil para adaptar modelos a novas tarefas ou categorias com um número limitado de exemplos, melhorando a flexibilidade e a capacidade de generalização do modelo.

**Exemplo Prático**: Um modelo de reconhecimento de texto manuscrito pode aprender a identificar uma nova letra ou símbolo com apenas um exemplo, facilitando a adaptação a diferentes estilos de escrita.

>> ### N-Shot
**Definição**: N-shot learning refere-se ao treinamento de um LLM com vários exemplos para aprender uma nova tarefa.

**Detalhamento**: A abordagem N-shot fornece ao modelo uma quantidade maior de exemplos, o que pode melhorar a precisão e a eficiência na realização da tarefa.

**Exemplo Prático**: Em um sistema de classificação de imagens, o N-shot learning pode ser utilizado para treinar o modelo com vários exemplos de diferentes categorias, melhorando sua capacidade de distinguir entre essas categorias.

## LoRA Quantizado (Adaptadores de Baixa Classificação)
**Definição**: LoRA quantizado é uma técnica para reduzir o tamanho e a complexidade dos LLMs, tornando-os mais adequados para execução em dispositivos com recursos limitados.

**Detalhamento**: A técnica envolve a aplicação de quantização e adaptadores de baixa classificação para compactar o modelo, permitindo sua execução eficiente em dispositivos com capacidade limitada.

**Exemplo Prático**: Aplicações móveis que utilizam LLMs para sugestões de texto em tempo real podem empregar LoRA quantizado para funcionar eficientemente em smartphones com processamento limitado, garantindo uma experiência de usuário fluida e rápida.

## Ajuste Fino com Eficiência de Parâmetros (Parameter-Efficient Fine-Tuning)
**Definição**: Ajuste fino com eficiência de parâmetros é uma técnica que permite treinar um modelo menor com base em um modelo maior, focando em uma tarefa específica e mantendo o uso de recursos controlado.

**Detalhamento**: Em vez de treinar um modelo do zero, que pode ser extremamente caro e demorado, essa abordagem permite adaptar um modelo pré-treinado a uma nova tarefa com um conjunto menor de dados. O ajuste fino concentra-se em otimizar o desempenho do modelo para tarefas específicas, como tradução de linguagem ou análise de sentimentos, sem a necessidade de recomeçar o treinamento.

**Exemplo Prático**: Imagine um modelo de linguagem geral como o GPT-3, que é treinado em uma vasta gama de dados. Para uma aplicação específica, como assistência jurídica, um modelo menor pode ser ajustado usando dados específicos do domínio jurídico. Esse processo permite que o modelo menor se especialize em gerar respostas ou documentos legais com base em uma base de conhecimento mais restrita, enquanto ainda se beneficia do conhecimento prévio do modelo maior.


## RAG (Geração Aumentada de Recuperação)
**Definição**: RAG é uma técnica onde um LLM não apenas gera texto, mas também recupera informações relevantes de fontes externas para aprimorar suas respostas.

**Detalhamento**: A Geração Aumentada de Recuperação combina a geração de texto com a recuperação de informações, permitindo que o modelo forneça respostas mais informadas e precisas ao buscar dados relevantes além do seu treinamento inicial.

**Exemplo Prático**: Em um assistente virtual avançado, o RAG pode ser usado para responder perguntas sobre eventos recentes ou informações específicas consultando fontes externas, como notícias ou bases de dados, para fornecer respostas atualizadas e detalhadas.

## Prompt Engineering
**Definição**: Prompt Engineering é a arte de criar instruções claras e específicas para orientar um LLM a gerar o resultado desejado.

**Detalhamento**: A engenharia de prompts envolve a elaboração de perguntas ou comandos precisos para obter respostas mais relevantes e úteis do modelo, maximizando a eficácia das interações com o LLM.

**Exemplo Prático**: Em um sistema de geração de conteúdo, a engenharia de prompts pode ser usada para formular instruções específicas para o LLM criar artigos, blogs ou textos que atendam a requisitos de estilo e conteúdo precisos.

---

Esta lista apenas arranha a superfície da linguagem LLM! À medida que o campo continua a evoluir, o mesmo acontece com o vocabulário. Mas com esses termos básicos você conseguirá navegar nesse mundo de IA, LLMs e GenAI.

Até o próximo post!
