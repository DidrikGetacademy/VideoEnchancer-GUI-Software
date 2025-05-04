from huggingface_hub import snapshot_download
import os



def download_deepseek_coder_7b_instruct():
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------

    
    Ideal Use Cases: 
    ------------------------------------------------------------------------
    
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
    """
    Model Features ----> 
    ------------------------------------------------------------------------
    
    Ideal Use Cases: 
    ------------------------------------------------------------------------


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




if __name__ == "__main__":
