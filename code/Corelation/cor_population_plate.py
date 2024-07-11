import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/district.csv')

# 将communityAverage的值分成20个等间隔的区间
df['communityAverage_category'] = pd.cut(df['communityAverage'], bins=50, labels=False)

# 计算每个区间的buildingType_plate的平均值
average_by_communityAverage_category = df.groupby('communityAverage_category')['buildingType_plate'].mean().reset_index()

# 使用Seaborn绘制点状图
sns.scatterplot(data=average_by_communityAverage_category, x='communityAverage_category', y='buildingType_plate')

# 为图表添加标题
plt.title('communityAverage Category vs. buildingType_plate')

# 显示图表
plt.show()