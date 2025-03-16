# -*- coding: utf-8 -*-
"""dev_cuda.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Lukeasargen/GarbageML/blob/main/dev_cuda.ipynb
"""

import torch

torch.cuda.get_arch_list()

for gpu_num in range(torch.cuda.device_count()):
    print(f"DEVICE:{gpu_num}")
    print(torch.cuda.get_device_properties(gpu_num))
    print(torch.cuda.memory_summary(gpu_num))

# print(f"{torch.cuda.memory_snapshot()=}")

print(f"{torch.cuda.memory_allocated()=}")
print(f"{torch.cuda.max_memory_allocated()=}")
print(f"{torch.cuda.memory_reserved()=}")
print(f"{torch.cuda.max_memory_reserved()=}")
print(f"{torch.cuda.memory_cached()=}")
print(f"{torch.cuda.max_memory_cached()=}")

for key, val in torch.cuda.memory_stats().items():
    print(f"{key}: {val}")

# 1 GBb = 1024*1024*1024 bytes
# torch.rand defaults to torch.float32 = 4 bytes
# this creates a 1GB tensor and puts it on the cuda:0
device = torch.device("cuda:0")
x = torch.rand(1, 256, 1024, 1024, requires_grad=False).to(device)

del x
torch.cuda.empty_cache()