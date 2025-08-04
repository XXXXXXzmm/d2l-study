"""
向量积

用矩阵的每一行与向量做 “点积”，得到结果向量的对应元素。 点积就乘积之后求和
需要注意的是 向量的长度必须和矩阵的列数一致！
"""
import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
x = torch.arange(4, dtype=torch.float32)

print(A.shape)
print(A)
print(x.shape)
print(x)
print(torch.mv(A, x))
