# Local LMM Software

- [FastChat](https://github.com/lm-sys/FastChat)
- [Oobabooga](https://github.com/oobabooga/text-generation-webui)
- [Jan.ai](https://jan.ai/) ***
- [Ollama](https://ollama.com/) ***
- [LocalAI](https://localai.io/) ** Docker
- [LlamaEdge](https://llamaedge.com/) ** Linux
- [GPT4All](https://gpt4all.io/) ***
- [LocalAI](https://www.localai.app/)
- [ArgalAi](https://argalai.com/)
- [Pinokio](https://pinokio.computer/)

Open WebUI - https://github.com/open-webui/open-webui
Lobe Chat - https://github.com/lobehub/lobe-chat
Chatbot-Ollama - https://github.com/ivanfioravanti/chatbot-ollama
BakLLaVA - https://github.com/Fuzzy-Search/realtime-bakllava
Text Generation WebUI (Oobabooga) - https://github.com/oobabooga/text-generation-webui


Existem várias ferramentas disponíveis para executar LLMs localmente, cada uma com seus próprios recursos e requisitos. Aqui estão algumas opções populares:

1. **LLaMA** (https://github.com/facebookresearch/llama)
  - Desenvolvido pela Meta (Facebook AI Research)
  - Modelos de código aberto disponíveis em vários tamanhos
  - Requisitos: GPU com pelo menos 24 GB de VRAM para o modelo maior

2. **Vicuna** (https://github.com/lm-sys/FastChat)
  - Modelo de código aberto semelhante ao ChatGPT
  - Desenvolvido pela Anthropic e aprimorado pela Lionsys
  - Requisitos: GPU com pelo menos 16 GB de VRAM

3. **Alpaca** (https://github.com/tatsu-lab/stanford_alpaca)
  - Modelo de código aberto semelhante ao GPT-3
  - Desenvolvido pela Stanford University e pela Anthropic
  - Requisitos: GPU com pelo menos 16 GB de VRAM

4. **Jurassic-1** (https://github.com/AI21Labs/jurassic-1-open-source)
  - Modelo de código aberto treinado pela AI21 Labs
  - Suporte a várias tarefas, incluindo geração de texto, tradução e análise de sentimentos
  - Requisitos: GPU com pelo menos 16 GB de VRAM

5. **GPT4All** (https://github.com/nomic-ai/gpt4all)
  - Implementação de código aberto do GPT-3.5 e GPT-4
  - Desenvolvido pela Nomic AI
  - Requisitos: GPU com pelo menos 24 GB de VRAM para o modelo GPT-4

6. **LM Studio** (https://lmstudio.ai/)
   - Interface de usuário baseada em navegador para LLMs
   - Suporta vários modelos, incluindo GPT-J, LLaMA, Vicuna, entre outros
   - Requisitos: GPU com pelo menos 16 GB de VRAM

7. **Ollama** (https://www.ollama.com/)
   - Aplicativo de desktop para executar LLMs localmente
   - Suporta LLaMA, Vicuna, Claude, Alpaca, entre outros
   - Requisitos: GPU com pelo menos 16 GB de VRAM




Existem várias ferramentas disponíveis que permitem executar LLMs diretamente em seu computador. Aqui estão algumas das principais:

### 1. Hugging Face Transformers

- **Website/Repositório:** [Hugging Face Transformers GitHub](https://github.com/huggingface/transformers)
- **Descrição:** Uma biblioteca que fornece modelos pré-treinados para tarefas de PLN (Processamento de Linguagem Natural), permitindo a fácil implementação de modelos como BERT, GPT-2, T5, entre outros.
- **Requisitos:** Python, PyTorch ou TensorFlow. Recomenda-se uma GPU para tarefas intensivas.

### 2. OpenAI GPT-3

- **Website/Repositório:** Disponível apenas via API para uso em nuvem; para uma versão local, pode-se utilizar implementações não oficiais ou versões anteriores como o GPT-2.
- **Descrição:** GPT-3 é um dos modelos mais avançados, oferecendo habilidades impressionantes de geração de texto.
- **Requisitos:** Para versões anteriores (GPT-2), Python e TensorFlow ou PyTorch. GPU é fortemente recomendada.

### 3. EleutherAI GPT-Neo e GPT-J

- **Website/Repositório:** [EleutherAI GitHub](https://github.com/EleutherAI)
- **Descrição:** Projetos open source que visam replicar e expandir as capacidades do GPT-3. GPT-Neo e GPT-J são alternativas acessíveis para uso local.
- **Requisitos:** Python, TensorFlow ou PyTorch. Uma GPU é essencial para desempenho eficiente.




Executar LLMs localmente oferece vantagens e desvantagens em comparação com serviços na nuvem, como ChatGPT, Microsoft Copilot ou Claude.ai.

**Vantagens:**
- **Privacidade**: Seus dados e consultas permanecem em seu computador, sem envio para servidores externos.
- **Controle**: Você tem controle total sobre o modelo, podendo ajustar parâmetros, realizar fine-tuning e personalizar o comportamento de cada modelo.
- **Custo**: Após o investimento inicial em hardware (computador, placa de video, etc), os custos de execução são menores ou praticamente inexistentes, em comparação com os serviços baseados em assinatura.

**Desvantagens:**
- **Requisitos de hardware**: É necessário um computador poderoso (mais ou menos), especialmente com GPUs (placa de vídeo) de alta capacidade, o que pode ser um pouco caro ou ainda não acessível para muitas pessoas.
- **Manutenção**: Você é responsável por atualizar, otimizar e solucionar problemas com os modelos e software.
- **Recursos limitados**: Os modelos de código aberto geralmente têm recursos menores que os modelos proprietários usados por serviços na nuvem.

**Fatores a considerar:**
- **Velocidade de processamento**: Executar LLMs localmente requer uma GPU poderosa para obter tempos de resposta aceitáveis. Modelos maiores exigem GPUs com mais VRAM.
- **Privacidade de informações**: Se a privacidade é uma preocupação crítica, executar localmente é a melhor opção, pois seus dados não deixam seu computador.
- **Uso pretendido**: Para tarefas que exigem grande personalização ou controle, executar localmente pode ser preferível. Para uso casual, serviços na nuvem podem ser mais convenientes.

Em geral, executar LLMs localmente oferece mais controle e privacidade, mas requer um investimento significativo em hardware e manutenção. Serviços na nuvem são mais convenientes, mas têm custos recorrentes e limitações devido à natureza proprietária dos modelos.

### Vantagens e Desvantagens

- **Vantagens de Rodar Localmente:**
  - Controle completo sobre os dados e modelos.
  - Não depende de conexões de internet ou serviços externos.
  - Customização mais flexível dos modelos.

- **Desvantagens de Rodar Localmente:**
  - Requer investimento significativo em hardware, especialmente em GPUs.
  - Maior complexidade na configuração e manutenção dos modelos.
  - Atualizações e manutenção do modelo são responsabilidade do usuário.

- **Vantagens na Nuvem:**
  - Acesso a modelos mais recentes e poderosos sem necessidade de hardware específico.
  - Facilidade de uso e integração com outras aplicações via APIs.
  - Custos inicialmente menores sem a necessidade de hardware próprio.

- **Desvantagens na Nuvem:**
  - Dependência de uma conexão de internet estável.
  - Possíveis preocupações com a privacidade e segurança dos dados.
