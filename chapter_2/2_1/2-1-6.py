"""
转换位 np 数组
"""
import torch

X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
A = X.numpy()
print(type(A))
print(type(X))