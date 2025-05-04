from huggingface_hub import snapshot_download
import os



def download_deepseek_coder_7b_instruct():
    """Advanced code generation and completion.
    Model Inseight---->
    ------------------------------------------------------------------------
    -6.7 billion parameters.
    -Context Length: 16K tokens.
    -Architecture: Transformer-based model optimized for code tasks, featuring a fill-in-the-blank objective for project-level code completion and infilling.
    -Training Data: 2 trillion tokens comprising 87% code and 13% natural language in English and Chinese.
    Model Features ----> 
    ------------------------------------------------------------------------
    -Supports project-level code completion and infilling.
    -Pre-trained on repository-level code corpus.
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Code generation, completion, and understanding tasks.
    """
    model_repo = "deepseek-ai/deepseek-coder-6.7b-instruct"
    local_dir = "./local_model/deepseek-coder-6.7b-instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ deepseek-coder-6.7b-instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")





def download_Mistral_7B_Instruct_v02():
    """General-purpose language understanding and generation.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 7.3 billion parameters.
    -Context Length: 32K tokens.
    -Architecture: Transformer model utilizing Grouped-Query Attention (GQA) and Sliding Window Attention (SWA) mechanisms for efficient long-context processing.
    -Training Data: The base model, Mistral-7B-v0.2, was pre-trained on publicly available datasets. The instruct version was fine-tuned to enhance instruction-following capabilities.
   
    Model Features ----> 
    ------------------------------------------------------------------------
    -Fine-tuned version of Mistral-7B-v0.1 with improved instruction-following capabilities.
    -Enhanced performance in tasks like mathematics, code generation, and reasoning.


    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Instruction-following tasks, content generation, and general-purpose language tasks.
    
    """
    model_repo = "Mistral-7B-Instruct-v0.2"
    local_dir = "./local_model/Mistral-7B-Instruct-v0.2"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Mistral-7B-Instruct-v0.2 downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")









def download_Qwen_Coder2_5_Instruct_1_5b():
    """Lightweight model for instruction-following tasks.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 1.5 billion parameters
    -Context Length: 32K tokens.
    -Architecture: Transformer architecture with Rotary Positional Embeddings (RoPE), SwiGLU activation, RMSNorm, Attention QKV bias, and tied word embeddings.
    -Training Data: Pre-trained and post-trained on a diverse corpus, including code, mathematical problems, and natural language data. Specific token counts are not disclosed.
    Model Features ----> 
    ------------------------------------------------------------------------
    -Suitable for environments with limited computational resources.
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Instruction-following tasks in resource-constrained settings
    
    """
    model_repo = "Qwen/Qwen2.5-1.5B-Instruct"
    local_dir = "./local_model/Qwen2.5-1.5B-Instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Qwen2.5-1.5B-Instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")




def download_Qwen_7b_Instruct_1M():
    """Handling tasks requiring long-context understanding.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 7.6 billion parameters.
    -Context Length: Up to 1 million tokens.
    -Architecture: Transformer architecture with RoPE, SwiGLU, RMSNorm, Attention QKV bias, and tied word embeddings.
    -Training Data: Enhanced for long-context understanding through long-context pre-training and post-training techniques. Specific datasets and token counts are not detailed.
    
    Model Features ----> 
    ------------------------------------------------------------------------
    -Optimized for long-context tasks.

    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Processing long documents, extended conversations, and other long-context scenarios.
    """
    model_repo = "Qwen/Qwen2.5-7B-Instruct-1M"
    local_dir = "./local_model/Qwen2.5-7B-Instruct-1M"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Qwen2.5-7B-Instruct-1M downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")










def download_Qwen_Coder_Instruct_7b():
    """Code generation and understanding.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 7.6 billion parameters.
    -Context Length: 128K tokens.
    -Architecture: Transformer architecture with RoPE, SwiGLU, RMSNorm, Attention QKV bias, and tied word embeddings.
    -Training Data: Trained on 5.5 trillion tokens, including source code, text-code grounding data, and synthetic data.
    Model Features ----> 
    ------------------------------------------------------------------------
    -Instruction-tuned for code-related tasks.
    -Enhanced code reasoning and generation capabilities.
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Code generation, debugging, and code-related instruction tasks
    """
    model_repo = "Qwen/Qwen2.5-Coder-7B-Instruct"
    local_dir = "./local_model/Qwen/Qwen2.5-Coder-7B-Instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Qwen2.5-Coder-7B-Instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")








def download_Qwen2_5_Coder_3B_Instruct():
    """ Efficient code generation in resource-constrained environments.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 3 billion parameters.
    -Context Length: 32K tokens.
    -Architecture: Transformer architecture with RoPE, SwiGLU, RMSNorm, Attention QKV bias, and tied word embeddings.
    -Training Data: Similar to its 7B counterpart, it was trained on 5.5 trillion tokens encompassing source code, text-code grounding data, and synthetic data. 
    
    Model Features ----> 
    ------------------------------------------------------------------------
    -Instruction-tuned for code-related tasks.
    -Balanced performance and resource usage.

    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Code generation and understanding in environments with limited computational resources
    """
    model_repo = "Qwen/Qwen2.5-Coder-3B-Instruct"
    local_dir = "./local_model/Qwen/Qwen2.5-Coder-3B-Instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Qwen2.5-Coder-3B-Instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")





def download_microsoft_Phi_3_mini_128k_instruct():
    """Lightweight model for instruction-following tasks with long-context support.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 3.8 billion parameters.
    -Context Length: 128K tokens.
    -Architecture: Dense decoder-only Transformer model fine-tuned with Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) to ensure alignment with human preferences and safety guidelines.
    -Training Data: Utilized the Phi-3 datasets, which include synthetic data and filtered publicly available website data, focusing on high-quality and reasoning-dense content. 
   
    Model Features ----> 
    ------------------------------------------------------------------------
    -Trained on synthetic and filtered public data focusing on high-quality, reasoning-dense content.
    -Supports long-context tasks in resource-constrained environments.

    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Ideal Use Cases: Instruction-following tasks requiring long-context understanding in environments with limited resources

    """
    model_repo = "microsoft/Phi-3-mini-128k-instruct"
    local_dir = "./local_model/microsoft/microsoft/Phi-3-mini-128k-instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ microsoft/Phi-3-mini-128k-instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")





def download_microsoft_Phi_4_mini_instruct():
    """ A lightweight, efficient model optimized for environments with limited computational resources.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 3.8 billion parameters
    -Context Length: 128K tokens
    -Architecture: Dense decoder-only Transformer
    -Training Data: 5 trillion tokens
     Model Features ----> 
    ------------------------------------------------------------------------
    -Designed for memory and compute-constrained environments.
    -Supports a 128K token context length.
    -Trained on synthetic and filtered public data, focusing on high-quality, reasoning-dense content.
    -Incorporates supervised fine-tuning and direct preference optimization for precise instruction adherence and robust safety measures.

    Ideal Use Cases: 
    ------------------------------------------------------------------------
    -Mobile applications, 
    -edge devices,
    -scenarios where low latency and efficient performance are critical
    
    """
    model_repo = "microsoft/Phi-4-mini-instruct "
    local_dir = "./local_model/microsoft/microsoft/Phi-4-mini-instruct "
    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ microsoft/microsoft/Phi-4-mini-instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")



def download_microsoft_Phi_4_multimodal_instruct():
    """A versatile model capable of processing and understanding multiple modalities, including text, images, and audio.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size: 5.6 billion parameters
    -Context Length: 128K tokens
    -Architecture: Multimodal model integrating text, vision, and speech/audio inputs
    Training Data: 
     5 trillion text tokens
     2.3 million hours of speech data
     1.1 trillion image-text tokens
    
    Model Features ---> Handles text, image, and audio inputs, generating text outputs.
    ------------------------------------------------------------------------
    -Supports a 128K token context length.
    -Text: Supports 24 languages
    -Vision: Primarily English.
    -Audio: English, Chinese, German, French, Italian, Japanese, Spanish, Portuguese.

    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    Applications requiring multimodal understanding, such as 
    virtual assistants that interpret 
    -images 
    -audio,
    -tools that analyze documents combining text and visuals
    """
    model_repo = "microsoft/Phi-4-multimodal-instruct"
    local_dir = "./local_model/microsoft/microsoft/Phi-4-multimodal-instruct"
    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ microsoft/Phi-4-multimodal-instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")




def download_microsoft_microsoft_Phi_4_reasoning_plus():
    """A model fine-tuned for advanced reasoning tasks, particularly in mathematics, science, and coding.
    Model Inseight---->
    ------------------------------------------------------------------------
    -Model Size:  14 billion parameters
    -Context Length: 32K tokens (extendable up to 64K tokens)
    -Architecture: Dense decoder-only Transformer
    Trainingdata:
    -Supervised Fine-Tuning (SFT): Over 1.4 million prompts and high-quality answers containing long reasoning traces generated using OpenAI's o3-mini model. The datasets cover topics in STEM (science, technology, engineering, and mathematics), coding, and safety-focused tasks
    -Reinforcement Learning (RL): Approximately 6,000 high-quality math-focused problems with verifiable solutions

    Model Features --->
    --------------------------------------------------------------------------------------
    -Built upon the base Phi-4 model with 14 billion parameters.
    -Supports a 32K token context length, extendable up to 64K for complex tasks.
    -Fine-tuned using supervised learning on chain-of-thought datasets and reinforcement learning for enhanced reasoning capabilities.
    -Generates detailed reasoning steps followed by concise summaries.
    
    Ideal Use Cases: 
    --------------------------------------------------------------------------------------
    -Tasks requiring deep analytical thinking, such as complex problem-solving in mathematics, 
    -cientific research
    -advanced coding challenges
    """
    model_repo = "microsoft/Phi-4-reasoning-plus"
    local_dir = "./local_model/microsoft/microsoft/microsoft/Phi-4-reasoning-plus"
    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ microsoft/Phi-4-reasoning-plus downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")





def test_infernece_and_modelloading_time():

if __name__ == "__main__":
