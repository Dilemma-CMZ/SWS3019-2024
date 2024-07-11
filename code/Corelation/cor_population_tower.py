import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/district.csv')

# 将communityAverage的值分成20个等间隔的区间
df['communityAverage_category'] = pd.cut(df['communityAverage'], bins=20, labels=False)

# 计算每个区间的buildingType_towel的平均值
average_by_communityAverage_category = df.groupby('communityAverage_category')['buildingType_towel'].mean().reset_index()

# 使用Seaborn绘制点状图
sns.scatterplot(data=average_by_communityAverage_category, x='communityAverage_category', y='buildingType_towel')

# 为图表添加标题
plt.title('communityAverage Category vs. buildingType_tower')

# 显示图表
plt.show()