"""
降维
"""
import numpy as np
import torch
# 对张量进行求和 就是一种降维操作
x = torch.arange(4, dtype=torch.float32)

# 从 向量 -> 标量
print(x)
print(x.sum())

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A)
print(A.shape)
print(A.sum())

# 默认情况的降维操作，是按照所有轴进行降维，相同的我们可以对某一个轴进行降维
A_sum_axis0 = A.sum(axis=0)
print(A_sum_axis0)
print(A_sum_axis0.shape)

A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1)
print(A_sum_axis1.shape)

# 还可以指定多个轴，在当前实例之下指定0,1 轴 就等同于 A.sum()
A_sum_axis0_1 = A.sum(axis=[0, 1])
print(A_sum_axis0_1)
print(A_sum_axis0_1.shape)

# 求平均值 numel 返回元素数量
print(A.mean())
print(A.sum() / A.numel())
# 求平均值也可以指定维度
print(A.mean(axis=0))
print(A.sum(axis=0) / A.shape[0])


# 有时候计算不想降低维度
# 可以使用 keepdims=True 来保持维度
sum_A = A.sum(axis=1, keepdims=True)
print(sum_A)

# 使用广播机制 todo:没弄懂具体的机制
print(A)
print(A / sum_A)

# 在不降维的情况下对某一轴进行累加
print(A.cumsum(axis=0))
