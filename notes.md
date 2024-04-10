# Roadmap Estudos AI

## Como posso começar a aprender AI

Você pode começar seus estudos sobre IA independente de qual seja a sua persona

- Usuário Final
- Super Usuário/Usuário Avançado
- Desenvolvedor
- Pesquisador

## Usuário

Não há melhor maneira de aprender sobre IA do que usando e experimentando. 

O primeiro passo do camiinho, é se tornar um usuário das ferramentas de IA. Você deve se cadastrar e criar sua conta em algumas ferramentas (veja lista abaixo) de IA generativa e vá usando para ganhar experiência e prática.Você deve se familiarizar com essas ferramentas de IA generativa, entender o que são, o que fazem, suas capacidades e recursos, enfim, colocar a mão na massa.

  - [ChatGPT](https://chat.openai.com/)
  - [Google Gemini](https://gemini.google.com/app)

## Super Usuário/Usuário Avançado

Depois de conseguir experiência prática com as ferramentas de IA, o próximo passo é aprimorar o conhecimento e aprender a usar melhor as ferramentas.

As ferramentas de IA generativa têm muito potencial, que ainda não foi explorado. Precisamos aprender a aplicar as técnicas corretas para usá-las de forma eficaz. A maioria das ferramentas de IA generativa gera respostas com base na descrição natural conhecida como prompt. Escrever rapidamente é uma arte. Precisamos aprender detalhadamente sobre a engenharia imediata para explorar todo o potencial da IA ​​generativa. Aqui está o que você precisa fazer para isso:

Saiba mais sobre a Prompt Engineering .
Explore as melhores e mais eficazes instruções para usar as ferramentas de IA generativa.
Entenda as práticas recomendadas para escrever prompts.



ELi5: Absolute beginner's guide to getting started in A.I. Image generation.
Tutorial - Guide
This question seems to be asked on a daily basis lately, so instead of having to answering them all the time, I've decided to just write a post so that I can link to it.

Since this is r/StableDiffusion, the usual answer offered is that one should start installing SD generators such as Automatic1111, ComfyUI, Fooocus, Forge, etc. That would have been the right answer one year ago but with all the free online generator available now, IMO this is no longer the best starting point for the absolute beginner.

The best way to learn anything is to get over the first speed bump as quickly as possible and start experimenting and have fun. So IMO the best way is to head over to https://www.bing.com/images/create and start playing with generative A.I. DALLE3 is currently the most advanced free A.I. generation system, in the sense that it is better at "following/understanding" the prompt/description of the image that user give to it. (Edit: at the moment, I cannot recommend using ideogram.ai https://ideogram.ai/ for the reason stated in one of the comments below).

But DALLE3 is a highly censored system, with so many guardrails that you can basically only generate "art" involving flower and puppies. No celebrities are allowed, at one point even some IP characters such as Batman are not allowed (sometimes they do allow it, the censor filter is updated all the time). DALLE3 has also been kneecapped so that it is bad at generating anything that look like real photography. Presumably this is so that people cannot produce anything even remotely titillating, and thus keeping the load on their server down to a manageable level, and to avoid any bad PR due to "deepfake/pornography".

Once you are bored or tired with the censorship/restrictions/limitations of bing/DALLE3, but you've learned enough about "text2img/prompting" that you feel Generative A.I. is something fun/useful. It is then time to graduate from kindergarten and go to elementary school by start using one of the Free Online SDXL Generators. https://www.reddit.com/r/StableDiffusion/comments/18h7r2h/free_online_sdxl_generators/

When you use these systems, make sure you choose one of the SDXL and not the SD1.5 models (See SDXL 1.0: a semi-technical introduction/summary for beginners if you want to know why, and to understand the difference between the various versions of SD). https://www.reddit.com/r/StableDiffusion/comments/15fj5k9/sdxl_10_a_semitechnical_introductionsummary_for/

Finally, a few very basic pointers about prompting. Prompting is the craft of writing a piece of text in such a way that the A.I. can "understand". The point to remember is that except for DALLE3, most generative A.I. systems such as SD actually does not understand language at all. Instead of a LLM (Large Language Model) SDXL actually uses something called CLIP (Contrastive Language–Image Pre-training) https://openai.com/research/clip which sort of associates images with words, and then use that association from text to image to guide the A.I. towards a certain type of images. It is a probabilistic model, which works well most of the time if the image is relatively simple, but it gets confused easily. So, the craft of "prompt engineering" is to write the prompt/description of the image you have in mind in such a way that you have a better chance of getting the desired result. This is often an iterative process, and at times involves "seed hunting" or "lucky seed". The most basics thing to remember is to follow a certain template, keeping in mind the what's "most important" about the image should come first in the description. So the general order of words in a prompt are:

1. The type of image you are trying to generate: photo, oil painting, watercolor, drawing, sketch, film still, etc.

2. The subject: Man, woman, cat, Taylor Swift, Batman, etc. Stick with one single main subject. Multiple subjects are hard to do due to something known as "concept bleeding" and will require more advanced techniques such as Regional Prompter https://github.com/hako-mikan/sd-webui-regional-prompter/tree/main

3. Action: holding an umbrella, playing soccer, eating spaghetti, etc.

4. Description of the subject: wearing a red dress, pink shoes, etc.

5. Description of the background, surrounding area: in the park, at a restaurant, black background, background is a swimming spool, etc.

6. Better prompting, how to get checkpoints to respond better to my prompts https://www.reddit.com/r/StableDiffusion/comments/1b5o4os/better_prompting_how_to_get_checkpoints_to/

7. How do you learn from other creators images? https://www.reddit.com/r/StableDiffusion/comments/1b7es6t/how_do_you_learn_from_other_creators_images/

Once you are comfortable with basic text2img, you can start learning more advanced topic such as "prompt weight aka attention/emphasis" https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#attentionemphasis, "prompt editing" https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#prompt-editing, etc. You should also learn about how to use different models, LoRAs, Control Net, Regional Prompter, etc. You can also start thinking about setting up a local installation of SD if you have the right hardware. GPU with over 6GiB of VRAM (not system RAM) is the bare minimum for running SDXL. As for which UI you should try, see What is the best GUI to install to use SD locally https://www.reddit.com/r/StableDiffusion/comments/17mobxj/what_is_the_best_gui_to_install_to_use_stable/? .

If you are curious about how all this A.I. black magic works, the not too technical best explanation is this Vox Video: https://youtu.be/SVcsDDABEkM?t=357 (Part 3: how it works start at 6:00). https://youtu.be/SVcsDDABEkM?t=357

I've not looked through the course myself, but maybe interesting to beginners: Free intro course to SD by Sebastian Kamph. https://www.reddit.com/r/StableDiffusion/comments/1b7f4tg/free_intro_course_to_stable_diffusion_by/


Free Online SDXL Generators
Resource - Update
People often ask about online generators, so I've decided to make a post rather than writing the same reply again. Even if you have a local setup (which is of course more flexible and maybe faster), these online generators are useful when you are away from your computer, and also for testing out models and LoRAs without having to download them.

My list consist only of free/semi-free sites that I've used personally. As for paid sites, there are just too many out there, and I've not tried them to have an opinion on them. But you are free to add comments about your favorite site here, of course.

There are of course the two generators from the 800 pound gorillas of internet: Bing/DALLE3 and Google's ImageFX/Imagine (but it is avaialble in US only?). There are also many free generators on discord, but I find them kind of clunky to use.

The information is up-to-date as of 2023-12-13, and I will try to keep it updated when things change. Please let me know if any information here is out of date by leaving a comment here.

tensor.art
100 free credits per day. Each generation can take between 0.5 to 1.2 credits, depending on the number of steps. Additional credits are required for the use of upscaling and ADetailer. Note: if you use one of the turbo mode SDXL models, you can use CFG:2, Sampler: DPM++ SDE Karra at just 5 steps, which means you can generate 500 SDXL images per day! This is a great way to test prompts.

ComfyUI is offered as an alternative UI (but custom nodes are not yet available): https://tensor.art/workflow

Most of the major models and LoRAs are available and can be used by free accounts.

NSFW generation are allowed, but there is some sort of filter, which I've never run into since I don't do NSFW.

ADetailer is supported for fixing faces.

Limited to 25 step (60 steps for paid)

Hi-res has maximum resolution of 1920x1080 (very high limit for paid)

Maximum of 3 LoRAs can be stacked (6 for paid)

Image that are not posted will only be retained for 15 days (60 for pro)

With the Pro account, you can also upload your own LoRAs for private use.

Tip: if the image generation seems to get stuck, just close or refresh the Workspace. Reopen the Workspace and wait a bit. Your image will show up eventually, or you will see "Exception" and you will have to regenerate it again.

civitai.com/generate
Currently free. In the future, SD1.5 will be free but SDXL will cost 3 buzz ($5 gets you 5000 buzz). It is very easy to get over 100 free buzz every day, though: https://civitai.com/user/buzz-dashboard

Cheap LoRA training (500 buzz or 20c per training)

Huge selection of models and LoRAs

Images can only be downloaded as JPEGs.

When images are uploaded to civitai the metadata will be parsed correctly.

Selection of sampler is limited (Just basics ones like DPM++ 2M Karras, Euler)

Some words are not allowed in prompts (for example, "dead"), but in general NSFW images are allowed (but currently blocked by OctoML, civitai's cloud provider, and civitai is in the process of finding new providers).

Quality is not as good as tensor.art, specially when LoRAs are used.

Newly uploaded LoRAs and models may not work, so you need to file bug reports.

No LoRA based on a real person can be used.

No ADetailer (yet)

No Hi-res (yet)

SeaArt.ai (Thanks to Ok-Vacation5730)
A large selection of models and LoRAs

Support LoRA training. Look under the "Train" tab and also "LoRA Template" for sample datasets.

150 Free "stamina" daily (Each SDXL image costs 6 stamina)

Wide range of resolutions to choose from

Images can be saved to folder without having to be posted publically.

Maximum of 40 steps

Maximum of 3 LoRAs (up to 5 for paid account)

Good selection of samplers

The user interface is still rough on the edge.

ADetailer is only available for SD1.5

Upscaler seems to produce poor quality images, at least none seems to work well for me when I tried it on SDXL models.

Tip: to use SDXL, you need to click on SDXL (right beside "Default") on the top right-hand corner, or you'll be wondering why the resolutions are all wrong, and why you cannot switch to SDXL models.

Make sure VAE is set to "auto".

To download the image as PNG, you need to click on the image to show it in full screen, then the option to download will appear. Or you can save it to a folder first.

withflare.ai
No limit on image generation

SDXL Base only.

Support for SDV

Support for DALLE3

Resolutions are limited to square, 16:9 and 9:16

Choice of Sampler is a bit limited

leonardo.ai (thanks to u/Ancient-Camel1636)
Besides their own propietary models, leonardo.ai also supports the following openly available models: AlbedoXL (a very fine merged model), SDXL 0.9 base, Deliberate 1.1, DreamShaper v5-v7, RPG v4/v5, and Absolute Reality 1.6.

Max resolution is 1536x1536

Cost is tied to resolution. For 512x512 the cost is 2 points. For 832x1216 the cost is 3.

Free plan: https://app.leonardo.ai/buy

150 fast generations per day, combined in any of the following ways: (I believe this is out of date, currently even 512x512 cost 2 points)

Up to 150 (768x768) generations per day

Up to 30 upscales or unzooms per day

Up to 75 background removals per day

Daily free tokens when your balance falls below 150

Other features/limitations:

Up to 1 pending jobs

Private generations

Priority infrastructure

Relaxed generation queue

No Concurrency

mage.space
Unlimited images per day

Only base SDXL/SD1.5/SD2.1. Many other models for paying customers.

LoRAs only for paying customers.

playgroundai.com
Only base SDXL/SD1.5/Playground V2/2.5 supported. But when you use SDXL there are many "filters" to choose from, and those filters have names such as "StarlightXL", "ZavyChromaXL", etc., so those filters are presumably LoRAs extracted from popular fine-tuned model.

500 images per day

Maximum resolution is 1024x1024

Limits on quality and details after 50 images

Create up to 3 canvas files

30 upscales per month

30 face restorations per month

ideogram.ai:
Not recommended due to inability to delete images.

New service with propietary model.

25 free prompts per day (4 images per prompt)

WARNING: image generate are public and cannot be deleted!

Image quality is soso, but prompt following seems to be quite good, maybe even DALLE3 level.

Censored just like DALLE3

Can generate image with moderate complexity involving more than one subject.

stablehorde.net
I also applaud the effort made by stablehorde.net for providing this valuable service to the community. The top 3 on my list, tensor.art, civitai.com, and seaarts.com probably stilll offer more models, but I've not used horde for a while, so horde's list of models and LoRAs may matches those services too. But in general, the free services I mentioned are faster than horde.

Here are some useful information for those to want to try stablehorde:

Image Generation
We provide a client interface requiring no installation and no technical expertise

We have also a few dedicated Web UIs with even less requirements:

Art Bot

Stable UI

AAAI UI

There are also mobile apps:

AI Painter (iOS + Android)

aislingeach (iOS)

There is also an older post about free and semi-free online generators: https://www.reddit.com/r/StableDiffusion/comments/15j6xdz/compilation_of_free_sdxl_image_generation_websites/


SDXL 1.0: a semi-technical introduction/summary for beginners
Tutorial | Guide
The question "what is SDXL?" has been asked a few times in the last few days since SDXL 1.0 came out, and I've answered it this way. The feedback was positive, so I decided to post it.

Here are some facts about SDXL from the StablityAI paper: SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis

A new architecture with 3.5B (6.6B if you include the refiner) parameters vs SD1.5/2.1's 860M parameters. My limited understanding with AI is that when the model has more parameters, it "understands" more things, i.e., it will have more concepts and ideas about the world crammed into it.

Better prompt following (see comment at the end about what that means). This is partly due to the larger model (since it understand more concept and ideas) and partly due to the use of dual CLIP encoders and some improvement in the underlying architecture that is beyond my level of understanding 😅

Better aesthetics through fine-tuning and RLHF (Reinforcement learning from human feedback).

Support for multiple native resolutions instead of just one for SD1.5 (512x512) and SD2.1 (768x768): SDXL Resolution Cheat Sheet and SDXL Multi-Aspect Training.

Enlarged 128x128 latent space (vs SD1.5's 64x64) to enable generation of high-res image. With 4 times more pixels, the AI has more room to play with, resulting in better composition and more interesting backgrounds.

Should I switch from SD1.5 to SDXL?
Many people are excited by SDXL because of the advances listed above (having played with SDXL extensively in the last few weeks, I can confirm the validity of these claims). If these advances are not important to you, then by all means stay with SD1.5, which is currently a more matured ecosystem, with many fine-tuned models to choose from, along with tons of LoRAs, TIs, ControlNet etc. It will be weeks if not months for SDXL to reach that level of maturity.

Edit: ControlNet is out: https://www.reddit.com/r/StableDiffusion/comments/15uwomn/stability_releases_controlloras_efficient/

Generating images with the "base SDXL" is very different from using the "base SD1.5/SD2.1" models because the "base SDXL" is already fine-tuned and produces very good-looking images. And if for some reason you don't like the new aesthetics, you can still take advantage of SDXL's new features listed above by running the image generated by SDXL through img2img or ControlNet with your favorite SD1.5 checkpoint model. For example, you can use this workflow: SDXL Base + SD 1.5 + SDXL Refiner Workflow : StableDiffusion

Are there any youtube tutorials?
SDXL Introduction by Scott Detweiler

SDXL and ComfyUI by Scott Detweiler

SDXL and Auto1111 by Aitrepreneur

Where can I try SDXL for free?
(See Free Online SDXL Generators for more detailed review)

These sites allow you to generate several hundred images per day for free, with minor restrictions such as no NSFW. Of course as a free user you'll be at the end of the queue and will have to wait for your turn 😁

tensor.art (100 free generations per day, all models and LoRAs hosted on the site are usable even for free accounts, NSFW allowed with no censorship.)

civitai.com (3 buzz point per images, but it is very easy to earn buzz.)

playgroundai.com (1024x1024 only, but allows up to 4 images per batch)

mage.space (one image at a time, but allows multiple resolutions)

clipdrop.co (this is the "official" one from StabilityAI, multiple resolutions, 4 images per batch, but contains watermark). Edit: apparently no longer working as a free service.

There are also the StabilityAI discord server bots: https://discord.com/invite/stablediffusion

Where can I find SDXL images with prompts?
Check out this Civitai collection of SDXL images ​

(Also check out I know where to find some interesting SD images)

What does "better prompt following" means?
It means that for any image that can be produced using SD1.5 where the image ACTUALLY followed the prompt (you can produce strange images when you let SD1.5 hallucinate where the prompt is not followed, and obviously SDXL will not be able to reproduce a similar nonsensical output), you can produce a similar image that embodies the same idea/concept using SDXL.

The reverse is not true. One can easily cook up a SDXL image that follows the prompt, and it would be very difficult if not impossible to craft an equivalent SD1.5 prompt.

SD1.5 is fine for expressing simpler ideas, and is perfectly capable of producing beautiful images. But the minute you want to make images with more complex ideas, SD1.5 will have a very hard time following the prompt properly. The failure rate can be very high with SD1.5 because you keep trying to hunt for the lucky seed or trying to tweak the prompt. With SDXL often you get what you want (assuming you are using the right model and have reasonable prompting skill) on the first try and just need some tweak to add detail, change background, etc.

Another frustrating thing about SD1.5 once you get used to SDXL is that SD1.5 images often lacks coherence and "mistakes" are much more common, hence the heavy use of word salad in the negative promp

But SD1.5 is better in the following ways:

Lower hardware requirement

Hardcore NSFW

"SD1.5 style" Anime (a kind of "hyperrealistic" look that is hard to describe). But some say AnimagineXL is very good. There is also Lykon's AAM XL (Anime Mix)

Asian Waifu

Simple portraiture of people (SD1.5 are overtrained for these type of images, hence better in terms of "realism")

Better ControlNet support.

Used to be faster, but with SDXL Lightning and Turbo-XL based models such as https://civitai.com/models/208347/phoenix-by-arteiaman one can now produce high quality images at blazing speed at 5 steps.

If one is happy with SD1.5, they can continue using SD1.5, nobody is going to take that away from them. For the rest of the world who want to expand their horizon, SDXL is a more versatile model that offer many advantages (see SDXL 1.0: a semi-technical introduction/summary for beginners). Those who have the hardware, should just try it (or use one of the Free Online SDXL Generators) and draw their own conclusions. Depending on what sort of generation you do, you may or may not find SDXL useful to you.

Anyone who doubt the versatility of SDXL based models, should check out https://civitai.com/collections/15937?sort=Most+Collected. Most of those images are impossible with SD1.5 models without the use of specialized LoRAs or ControlNet.