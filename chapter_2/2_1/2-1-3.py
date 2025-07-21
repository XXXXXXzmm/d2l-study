"""
广播机制 会自动的将不会纬度的向量扩充为一个大的向量
张量必须从右向左维度兼容
todo: 这里还是没有特别弄懂，还是要详细的理解一下
"""
import torch

x = torch.arange(3).reshape(3, -1)
y = torch.arange(2).reshape(-1, 2)
print(x)
print(y)
print(x + y)


X = torch.arange()