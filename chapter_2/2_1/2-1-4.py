"""
索引和切片
可以访问张量中的元素；或者截取一部分类似于子集的概念
"""
import torch

X = torch.arange(12, dtype=torch.float32).reshape((3, 4))

# todo: 这里多维怎么处理，或者我要取一列怎么处理
print(X)
print(X[0])
print(X[1:3])


# 给张量中特定的元素赋值
print(X[1, 2])
X[1, 2] = 9
print(X)

# 给张量中的元素进行批量赋值
# 这里的赋值是将 0 到 1 行的所有元素赋值为 12， 单独: 代表所有列
# 0:2 是一个左开右闭的区间，不包括0 包括 2
X[0:2, :] = 12
print(X)

