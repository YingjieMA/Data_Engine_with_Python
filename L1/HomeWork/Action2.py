# Action2: 统计全班的成绩
# 班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的
# 平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出
# （可以用numpy或pandas)

# 姓名|语文|数学|英语|
# 张飞|68|65|30|
# 关羽|95|76|98|
# 刘备|98|86|88|
# 典韦|90|88|77|
# 许褚|80|90|90|
import pandas as pd
data = {'姓名':['张飞','关羽','刘备','典韦','许褚'],'语文':[68,95,98,90,80],
'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df = pd.DataFrame(data)
print(df)
yuwen_mean = df['语文'].mean()
print('语文平均值: ',yuwen_mean)
yuwen_min = df['语文'].min()
print('语文最小值: ',yuwen_min)
yuwen_max = df['语文'].max()
print('语文最大值: ',yuwen_max)
yuwen_var = df['语文'].var()
print('语文方差: ',yuwen_var)
yuwen_std = df['语文'].std()
print('语文标准差: ',yuwen_std)
# 问题： df['总和'] = df[1:3].sum() 不行吗？
df['总和'] = df['语文']+df['数学']+df['英语']
print(df)
print(df.sort_values('总和', ascending=False))