"""
张量 和 标量 或者和相同形状的 张量运算 不会改变形状
"""
import torch
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()

print(A)

# 两个矩阵的乘法叫做 哈达玛积 就是相应的元素相乘
print(A * B)


# 张量和标量 运算不会改变形状，只是每个元素都和标量做运算
a = 2
X = torch.arange(20).reshape(5, 4)
print(X)
print(a + X)
print(a * X)

# 两个大小相同的矩阵相加/相乘，是矩阵相同位置的元素进行相加/相乘
print(A + B)
print(A * B)



