"""
矩阵乘法
和 哈达玛积 不是一个概念，需要进行区分

"""
import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = torch.ones((4, 3))

#得到的是 A 的行 x B的列这样的矩阵  所以不满足交换律除非是单位矩阵
print(A)
print(B)
print(torch.mm(A, B))
