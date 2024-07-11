import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/district.csv')

# 将communityAverage的值分成50个等间隔的区间
bins = 50
df['communityAverage_category'] = pd.cut(df['communityAverage'], bins=bins, labels=False)

# 计算每个区间的buildingType_towel的平均值
average_by_communityAverage_category = df.groupby('communityAverage_category')['buildingType_towel'].mean().reset_index()

# 为DataFrame添加百分比范围标签的列
average_by_communityAverage_category['percentage_range'] = average_by_communityAverage_category['communityAverage_category'].apply(
    lambda x: f"{x*100/bins}%~{(x+1)*100/bins}%"
)

# 使用Seaborn绘制点状图
sns.scatterplot(data=average_by_communityAverage_category, x='percentage_range', y='buildingType_towel')

# 为图表添加标题
plt.title('communityAverage Category vs. buildingType_towel')

# 显示图表
plt.xticks(rotation=90)  # 旋转x轴标签，以便它们更容易阅读
plt.show()

# 将点的坐标数据导出到CSV文件
average_by_communityAverage_category.to_csv('../../data/corelation/population_vs_tower.csv', index=False, columns=['percentage_range', 'buildingType_towel'])