"""
点积
即两个矩阵相同位置的元素 进行乘积然后求和运算

两个矩阵如果大小不同怎么办？必须要求一致

"""
import torch

x = torch.arange(4, dtype=torch.float32)
y = torch.ones(4, dtype=torch.float32)

print(x)
print(y)
print(torch.dot(x, y))
