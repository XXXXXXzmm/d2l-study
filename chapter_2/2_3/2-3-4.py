"""
张量
就是多阶的
在实际应用中我们对于 图片的处理 除了 RGB 的颜色通道以外还有通明通道  所以需要4阶
"""
import torch

X = torch.arange(24).reshape(2, 3, 4)
print(X)

