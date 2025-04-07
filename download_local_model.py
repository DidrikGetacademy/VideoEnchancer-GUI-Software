from huggingface_hub import snapshot_download

# Define the model repository and the local directory
model_repo = "Qwen/Qwen2.5-Coder-7B-Instruct"
local_dir = './local_model'

# Download the model to the specified directory
snapshot_download(repo_id=model_repo, local_dir=local_dir)
