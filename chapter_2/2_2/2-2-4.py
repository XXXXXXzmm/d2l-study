"""
练习
创建包含更多行和列的原始数据集。
    删除缺失值最多的列。
    将预处理后的数据集转换为张量格式。
"""
import os
import pandas as pd
import torch

data_file = os.path.join('..', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file)

miss_data_list = data.isna().sum()

max_col_name = ''
max_miss_count = 0
for col_name in miss_data_list.index:
    if miss_data_list[col_name] > max_miss_count:
        max_col_name = col_name
        max_miss_count = miss_data_list[col_name]

data = data.drop(max_col_name, axis=1)
print(data)

X = torch.tensor(data.to_numpy(dtype=float))
print(X)