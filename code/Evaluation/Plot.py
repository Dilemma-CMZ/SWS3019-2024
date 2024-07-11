import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

if __name__ == '__main__':
    col = 'Final_point'

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # 读取北京的地理数据
    bj = gpd.read_file('../../data/Beijing_shp')
    bj = bj.to_crs(epsg=4326)

    # 读取评估结果数据
    df = pd.read_csv('../../data/Evaluation_result_full.csv')

    # 确保两个DataFrame使用相同的列名进行合并
    # 假设共同的列名是'ID'
    bj = bj.merge(df, on='new_id', how='left')  # 使用'left'以保留所有bj中的行


    # 标准化数值
    values_normalized = (bj[col] - bj[col].min()) / (bj[col].max() - bj[col].min())

    # 设置颜色映射
    cmap = plt.get_cmap('viridis')
    colors = cmap(values_normalized)

    # 绘制地图，应用颜色映射
    bj.plot(ax=ax, column=col, cmap=cmap, legend=True, edgecolor='black')

    # 设置图表的标题和坐标轴标签
    ax.set_title('Beijing Evaluation Result')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()