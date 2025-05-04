from huggingface_hub import snapshot_download
import os



def download_deepseek_coder_7b_instruct():
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
