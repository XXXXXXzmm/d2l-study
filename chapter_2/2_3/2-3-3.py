"""
矩阵
可以理解为 2 阶张量
"""
import torch

A = torch.arange(20).reshape(5, 4)
print(A)

# 矩阵的转置 矩阵的转置本质上是关于主对角线的对称变换。
print(A.T)

# 存在一种特殊的矩阵 就是 转置矩阵和它本身是相同的
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)
print(B == B.T)