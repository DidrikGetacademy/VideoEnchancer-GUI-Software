import tensorflow as tf
print(tf.sysconfig.get_build_info()["cudnn_version"])
import torch
print(torch.backends.cudnn.version())
