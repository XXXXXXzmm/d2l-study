"""
节省内存
因为有时候张量很大，如果老是重新分配内存会导致内存的浪费
所以有时候情况允许的话，希望在原地进行操作
"""
import torch

X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

# id() 函数可以查看张量的内存地址
before = id(Y)
Y = Y + X
print(before)
print(id(Y))
print(id(Y) == before)

# 使用 [:] 表示原地操作
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))

