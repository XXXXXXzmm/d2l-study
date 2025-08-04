"""
将pd 读出来的 数值数据 转换为 张量
"""
import os
import pandas as pd
import torch

data_file = os.path.join('..', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
inputs = pd.get_dummies(inputs, dummy_na=True)

# 将pd读出来的值转换为张量
X = torch.tensor(inputs.to_numpy(dtype=float))
Y = torch.tensor(outputs.to_numpy(dtype=float))
print(X)
print(Y)

