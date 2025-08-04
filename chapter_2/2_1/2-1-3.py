"""
广播机制 会自动的将不会纬度的向量扩充为一个大的向量
张量必须从右向左维度兼容

满足广播的需求：
两个维度大小相同，可以直接匹配
其中一个维度为 1，可以广播到另一个维度的大小
其中一个张量没有该维度，可以自动添加维度并广播
"""
import torch

x = torch.arange(3).reshape(3, -1)
y = torch.arange(2).reshape(-1, 2)
print(x)
print(y)
print(x + y)


# 2.1.8.2 练习题
X = torch.arange(6).reshape(1, 2, 3)
Y = torch.arange(4).reshape(2, 2, 1)
print(X)
print(Y)
print(X + Y)
