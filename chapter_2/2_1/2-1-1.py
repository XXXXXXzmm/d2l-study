"""
2.1.1 数据预处理；基本操作
熟悉 troch 的基本操作
"""
import torch

# 创建一个张量 x ；如果是一维张量称之为向量；如果是二维张量称之为矩阵(线性代数中的举证)
x = torch.arange(12)
print(x)

# 输出 x 的形状
print(x.shape)

# 输出 x 元素个数
print(x.numel())

# 改变张量的形状使用 reshape； 下面是把 x 从行向量 -> 矩阵
# 需要注意的是 数量需要保持一致 多了少了都不行,
# 可以使用 -1 自动推断， 指定高或者宽为 -1 时，会自动推断, 必须有一列是确定！
# x = x.reshape(3, 4)
x = x.reshape(3, -1)
print(x)

# 快捷创建全部为0和全部为1的张量，只需要指定形状即可
print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))
print(torch.randn(3, 4))