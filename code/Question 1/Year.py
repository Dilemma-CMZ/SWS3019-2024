import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df0 = pd.read_csv('../../data/district.csv')
    df0 = df0[df0['year'] >= 2010]
    df0 = df0[df0['mall_cnt'] >= 13]
    df0 = df0[df0['mall_cnt'] <= 16]
    df0 = df0['belonging']

    df = pd.read_csv('../../data/house_belonging.csv')
    df = df[df['year'] >= 2010]
    df = pd.merge(df, df0, on='belonging', how='right')
    df = pd.get_dummies(df, columns=['buildingType'])
    df.rename(columns={'buildingType_1.0': 'buildingType_tower'}, inplace=True)
    df.rename(columns={'buildingType_2.0': 'buildingType_bungalow'}, inplace=True)
    df.rename(columns={'buildingType_3.0': 'buildingType_comb'}, inplace=True)
    df.rename(columns={'buildingType_4.0': 'buildingType_plate'}, inplace=True)
    df.info()

    df1 = df.groupby('year').mean()
    df1 = df1.reindex(columns=['year', 'buildingType_tower', 'buildingType_bungalow', 'buildingType_comb', 'buildingType_plate'])
    df1.info()
    df1.to_csv('../../data/q1_by_year.csv')

    df1 = pd.read_csv('../../data/q1_by_year.csv')
    plt.plot(df1['year'], df1['buildingType_tower'], label='tower')
    plt.plot(df1['year'], df1['buildingType_comb'], label='comb')
    plt.plot(df1['year'], df1['buildingType_plate'], label='plate')

    plt.title('')
    plt.xlabel('Year')
    plt.ylabel('Percent')
    plt.legend()
    plt.show()
