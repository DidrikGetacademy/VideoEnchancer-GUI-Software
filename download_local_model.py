from huggingface_hub import snapshot_download
import os

def download_Qwen_Coder_7B_Instruct():
    model_repo = "Qwen/Qwen2.5-Coder-7B-Instruct"
    local_dir = "./local_model/qwen_coder_7b_instruct"

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

def download_deepseek_coder_7b_instruct():
    model_repo = "deepseek-ai/deepseek-coder-6.7b-instruct"
    local_dir = "./local_model/deepseek_coder_7b_instruct"

    if not os.path.exists(local_dir):
        print(f"📥 Downloading {model_repo} into {local_dir}...")
        snapshot_download(
            repo_id=model_repo,
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ Deepseek-Coder-6.7B-Instruct downloaded successfully.")
    else:
        print(f"✅ Model already exists at {local_dir}, skipping download.")

if __name__ == "__main__":
    download_Qwen_Coder_7B_Instruct()