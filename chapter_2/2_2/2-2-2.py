"""
处理csv文件中缺失的列

"""
import pandas as pd
import os

data_file = os.path.join('..', 'data', 'house_tiny.csv')

data = pd.read_csv(data_file)

# iloc 函数的作用是 截取数据 第一个 : 表示所有行
# 这里的 0:2 表示 截取第 0 列和第 1 列 是一个 左闭右开区间
# 这里的 2 表示 截取第 2 列
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]

# mean 函数的作用是 求平均值，只针对数值类型
# fillna 函数的作用是 填充缺失值,填充为 NaN
inputs = inputs.fillna(inputs.mean())
print(inputs)

# pd.get_dummies() 函数的作用是 对离散值进行编码，也就是一个分类一列，然后取0或者1
# dummy_na=True 表示 缺失值也会被编码
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)

