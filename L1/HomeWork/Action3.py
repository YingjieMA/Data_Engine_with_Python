# Action3: 对汽车质量数据进行统计
# 数据集：car_complain.csv
# 600条汽车质量投诉
# Step1，数据加载
# Step2，数据预处理
# 拆分problem类型 => 多个字段
# Step3，数据统计
# 对数据进行探索：品牌投诉总数，车型投诉总数
# 哪个品牌的平均车型投诉最多
import pandas as pd
import numpy as np
# Step1，数据加载
result = pd.read_csv('car_complain.csv')
# Step2，数据预处理
result = result.drop(columns = ['problem']).join(result.problem.str.get_dummies(','))
tags = result.columns[7:]
# Step3，数据统计
df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df3 = result.groupby(['car_model'])[tags].agg(['sum'])
df2['brand_sum'] = df2.apply(lambda x: x.sum(), axis=1)
df3['car_model_sum'] = df3.apply(lambda x: x.sum(), axis=1)
# 提问：如何去除中间的hot-red编码列
print('品牌投诉总数')
print(df2)
print('车型投诉总数')
print(df3)
df.to_csv('temp1.csv', index=True,encoding='utf_8_sig')
df2.to_csv('temp2.csv', index=True,encoding='utf_8_sig')
df3.to_csv('temp3.csv', index=True,encoding='utf_8_sig')
# Step3，数据统计