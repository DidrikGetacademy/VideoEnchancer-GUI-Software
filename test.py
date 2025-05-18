import torch
print(torch.__version__)
import torch

print("CUDA available:", torch.cuda.is_available())
print("CUDA device:", torch.cuda.get_device_name(0))
print("CUDA version:", torch.version.cuda)
print("cuDNN version:", torch.backends.cudnn.version())
