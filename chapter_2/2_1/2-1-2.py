"""
2.1.2 数据预处理；运算符
熟悉 张量之间的运算
"""
import torch

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])

# 张量的常用运算符; ** 是 x^y(求幂)
# 这是最简单的运算，因为 元素数量是相同的点对点进行运算;后续会在线性代数里面讲解非对称矩阵的运算
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

# 实际是 e^x (e自然指数),其核心作用是将实数范围的输入映射到正数范围
print(torch.exp(x))

# 多个矩阵进行连接
X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(X)
print(Y)

# 这里是将 X Y 两个矩阵进行连接
# 这里的 0 表示 行连接， 1 表示列连接; dim 是维度的意思
print(torch.cat((X, Y), dim=0))
print(torch.cat((X, Y), dim=1))

# 构建二维张量，对 X 和 Y 中的元素进行一个一个的对比，相同就是 True, 不同就是False
print(X == Y)
# 2.1.8.1 练习题
print(X > Y)
print(X < Y)

# 输出张量 X 中所有元素的和
print(X.sum())

