import random

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    bj = gpd.read_file('Beijing_shp')
    bj = bj.to_crs(epsg=4326)
    bj.plot(ax=ax, color='lightgrey', edgecolor='0.8')
    bj.info()

    df = pd.read_csv('Mall.csv')
    for index, row in df.iterrows():
        ax.scatter(row['longitude'], row['latitude'], color='red', s=2)

    df = pd.read_csv('BeijingHousingPrices_preprocessed.csv')
    for index, row in df.iterrows():
        if random.randint(0, 99) == 1:
            ax.scatter(row['Lng'], row['Lat'], color='blue', s=2)

    ax.set_title('')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()
