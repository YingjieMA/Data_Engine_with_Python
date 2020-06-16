# 对汽车投诉信息进行分析
import pandas as pd
import numpy as np
#pd.read_csv将文件存为DataFrame
result = pd.read_csv('car_complain.csv')
# print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
# drop('problem', 1) 等同于 drop(columns = ['problem'])
result = result.drop(columns = ['problem']).join(result.problem.str.get_dummies(','))
print(result.columns)
# 取从7+列开始的数据
tags = result.columns[7:]
print(tags)
# groupby('A')['B'].agg(xx) 按A聚合，B列做为统计
# agg(['A','B','C']) 有几列对应加几列
df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
print(df2)
# left_index=True 根据index进行合并，而不是某一列
# pandas.merge(left.right) 或者 dataframe.merge(right)
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
# inplace=True不创建新对象，还原索引
df2.reset_index(inplace=True)
# 从大到小排列
df2= df2.sort_values('count', ascending=False)
print(df2.columns)
# index=False 不导出索引
df2.to_csv('temp.csv', index=False,encoding='utf_8_sig')
query = ('A14', 'sum')
print(df2.sort_values(query, ascending=False))
####################################
