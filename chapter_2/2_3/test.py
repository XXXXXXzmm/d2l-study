"""
测试题
"""
import torch

# 1.证明一个矩阵 A 的转置的转置是 A 本身
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.T.T
# print(A)
# print(B)
# print(A == B)
# print(torch.allclose(A, B))

# 2.给出两个矩阵 A 和 B 证明“它们转置的和”等于“它们和的转置” 转置分配率

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = torch.arange(20, dtype=torch.float32).reshape(5, 4)

C = A.T + B.T
D = (A + B).T
# print(C)
# print(D)
# print(C == D)
# print(torch.allclose(C, D))


# 3.给定任意方阵 A，A + A.T 总是对称的吗?为什么?
"""
对 C = A + Aᵀ求转置：
Cᵀ = (A + Aᵀ)ᵀ = Aᵀ + (Aᵀ)ᵀ （根据转置的分配律）
由于 (Aᵀ)ᵀ = A，因此 Cᵀ = Aᵀ + A = A + Aᵀ = C
"""
A = torch.arange(16, dtype=torch.float32).reshape(4, 4)
C = A + A.T
# print(torch.allclose(C, C.T))

# 4、对于张量X len(x) 输出的是张量X的第一个维度的大小
X = torch.arange(24).reshape(2, 3, 4)
# print(len(X))

# 5、对于任意形状的张量X,len(X)是否总是对应于X特定轴的长度?这个轴是什么?
# 是的，len(X) 输出的是张量X的第一个维度的大小，这个轴是0轴
# 对于一个张量 X；len(X) 等价于 X.shape[0]

# 6、运行A/A.sum(axis=1)，看看会发生什么。请分析一下原因？
# 维度不匹配 不能直接相除
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
# print(A)
# print(A.sum(axis=1))
# print(A / A.sum(axis=1))

# 7、考虑一个 (2, 3, 4) 的张量，在轴0、1、2上的求和输出是什么形状?
# 指定轴求和即指定的轴消失
# 轴0 消失 输出形状为 (3, 4)
# 轴1 消失 输出形状为 (2, 4)
# 轴2 消失 输出形状为 (2, 3)
A = torch.arange(24, dtype=torch.float32).reshape(2, 3, 4)
print(A)
print(A.sum(axis=0))
print(A.sum(axis=1))
print(A.sum(axis=2))