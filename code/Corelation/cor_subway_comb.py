import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/district.csv')

# 将subway的值分成20个等间隔的区间
df['subway_category'] = pd.cut(df['subway'], bins=10, labels=False)

# 计算每个区间的buildingType_comb的平均值
average_by_subway_category = df.groupby('subway_category')['buildingType_comb'].mean().reset_index()

# 使用Seaborn绘制点状图
sns.scatterplot(data=average_by_subway_category, x='subway_category', y='buildingType_comb')

# 为图表添加标题
plt.title('Subway Category vs. buildingType_comb')

# 显示图表
plt.show()