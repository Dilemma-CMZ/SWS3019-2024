import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

if __name__ == '__main__':
    col = 'Final_point'

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    bj = gpd.read_file('../../data/Beijing_shp')
    bj = bj.to_crs(epsg=4326)

    df = pd.read_csv('../../data/Evaluation_result_full.csv')

    bj = bj.merge(df, on='new_id', how='left')

    values_normalized = (bj[col] - bj[col].min()) / (bj[col].max() - bj[col].min())

    cmap = plt.get_cmap('coolwarm')
    colors = cmap(values_normalized)

    bj.plot(ax=ax, column=col, cmap=cmap, legend=True, edgecolor='black')

    ax.set_title('Beijing Evaluation Result')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()
