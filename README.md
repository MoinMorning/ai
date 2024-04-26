## GPT4All Unity Bindings

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) 

These are Unity3d bindings for [GPT4All](https://github.com/nomic-ai/gpt4all), providing high-performance inference of large language models (LLMs) running on your local machine.

> Please note: These bindings currently utilize an outdated version of GPT4All, lacking support for the latest model architectures and quantization. For more information, refer to [this issue](https://github.com/Macoron/gpt4all.unity/issues/11).

**Main Features:**
- Implementation of chat-based LLM suitable for NPCs and virtual assistants.
- Models available in various sizes for both commercial and non-commercial applications.
- High-speed CPU-based inference.
- Operates locally without requiring an internet connection.
- Free and open-source.

**Supported Platforms:**
- [x] Windows (x86_64)
- [x] MacOS (Intel and ARM)
- [ ] Linux
- [ ] iOS
- [ ] Android
- [ ] WebGL

## Samples

![Sample Image](https://github.com/Macoron/gpt4all.unity/assets/6161335/1c0540d0-a169-4d88-8661-35ec0681ff5b)

*"mpt-7b-chat" model, simulating a roleplaying dwarf NPC on a MacBook with M1 Pro*

## Getting Started
Clone this repository and open it as a regular Unity project. It should function properly starting from Unity 2019.4 LTS.

Alternatively, you can add this repository to your existing project as a **Unity Package**. Add it using the following git URL in your Unity Package Manager:
https://github.com/Macoron/gpt4all.unity.git?path=/Packages/com.gpt4all.unity

markdown
Copy code
### Downloading Model Weights

To utilize this library, you'll need to download model weights. You can find a full list of officially supported GPT4All models and their download links [here](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat#manual-download-of-models).

> Note: Some models may have restrictions for commercial projects. Please review their licenses before integrating them into your project.

After downloading a model, place it in the `StreamingAssets/Gpt4All` folder and update the path in the `LlmManager` component.

List of models tested in Unity:
- [mpt-7b-chat](https://huggingface.co/macoron/ggml-mpt-7b-chat) [license: cc-by-nc-sa-4.0]
- [mpt-7b-instruct](https://huggingface.co/macoron/ggml-mpt-7b-instruct) [license: cc-by-sa-3.0]
- [mpt-7b-base](https://huggingface.co/macoron/ggml-mpt-7b-base) [license: apache-2.0]
- [gpt4all-j-v1.3-groovy](https://huggingface.co/macoron/ggml-gpt4all-j-v1.3-groovy) [license: apache-2.0]
- gpt4all-l13b-snoozy

## Compiling C++ Libraries from Source
TBD

## License
This project is licensed under the MIT License.

It utilizes compiled libraries of [GPT4All](https://github.com/nomic-ai/gpt4all/tree/main) and [llama.cpp](https://github.com/ggerganov/llama.cpp), both also under the MIT license.

Models are not included in this repository. Please contact the original model creators to learn more about their licenses.

---

## GPT4All: On-Edge Large Language Models

GPT4All offers open-source large language models that operate locally on your CPU and nearly any GPU.

**GPT4All Website and Models** • **GPT4All Documentation** • **Discord**

![GPT4All Image](https://placekitten.com/200/300)
https://docs.gpt4all.io/

## GPT4All: An Ecosystem of Open-Source On-Edge Large Language Models

GPT4All provides the capability to run powerful and customized large language models directly on your local machine. These models are compatible with consumer-grade CPUs and GPUs. Your CPU needs to support AVX or AVX2 instructions.

For more details, refer to the documentation.

A GPT4All model typically ranges from 3GB to 8GB in size and can be downloaded and integrated into the GPT4All open-source ecosystem software. This software ecosystem is maintained by **Nomic AI**, ensuring quality, security, and ease of training and deploying your own on-edge large language models.

### What's New

- **Latest Release**: Explore the latest release.
- **October 19th, 2023**: GGUF Support Launches, featuring:
    - The Mistral 7b base model and an updated model gallery on gpt4all.io.
    - Several new local code models, including Rift Coder v1.5.
    - Nomic Vulkan support for Q4\_0 and Q4\_1 quantizations in GGUF.
    - Offline build support for running old versions of the GPT4All Local LLM Chat Client.
- **September 18th, 2023**: Nomic Vulkan launches, supporting local LLM inference on AMD, Intel, Samsung, Qualcomm, and NVIDIA GPUs.
- **August 15th, 2023**: GPT4All API launches, enabling inference of local LLMs from Docker containers.
- **July 2023**: Stable support for LocalDocs, a GPT4All Plugin that enables private and local chat with your data.

### Chat Client

You can run any GPT4All model natively on your home desktop using the auto-updating desktop chat client. Visit the GPT4All Website for a complete list of open-source models compatible with this powerful desktop application.

Direct Installer Links:
- macOS
- Windows
- Ubuntu

### Chat Client Building and Running

Follow the visual instructions on the chat client build_and_run page.

### Bindings

Official Bindings:
- Python Bindings !Downloads
- Typescript Bindings
- GoLang Bindings
- C# Bindings
- Java Bindings

### Integrations

- Weaviate Vector Database - Module Docs

## Citation

If you utilize this repository, models, or data in a downstream project, please consider citing it with:
```
@misc{gpt4all,
  author = {Yuvanesh Anand and Zach Nussbaum and Brandon Duderstadt and Benjamin Schmidt and Andriy Mulyar},
  title = {GPT4All: Training an Assistant-style Chatbot with Large Scale Data Distillation from GPT-3.5-Turbo},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nomic-ai/gpt4all}},
}
```
