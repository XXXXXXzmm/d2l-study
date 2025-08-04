"""
标量
单独的元素称之为标量
可以理解为 0 阶张量
"""
import torch

x = torch.tensor(3.0)
y = torch.tensor(4.0)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
