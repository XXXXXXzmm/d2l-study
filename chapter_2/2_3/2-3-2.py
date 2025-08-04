"""
向量
在python中向量可以被视为标量值组成的列表。
可以理解为1阶张量
"""
import torch

x = torch.arange(4)
print(x)

# 可以通过下标来引用向量中的值，这个值就是一个标量
print(x[3])

# 向量存在长度、维度
print(len(x))
print(x.shape)