import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/district.csv')

# 将subway的值分成20个等间隔的区间
df['subway_category'] = pd.cut(df['subway'], bins=20, labels=False)

# 计算每个区间的buildingType_bungalow的平均值
average_by_subway_category = df.groupby('subway_category')['buildingType_bungalow'].mean().reset_index()

# 使用Seaborn绘制点状图
sns.scatterplot(data=average_by_subway_category, x='subway_category', y='buildingType_bungalow')

# 为图表添加标题
plt.title('Subway Category vs. buildingType_tower')

# 显示图表
plt.show()