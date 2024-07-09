import pandas as pd

if __name__ == '__main__':
    df3 = pd.read_csv('../../data/BJ1.csv')
    df3 = df3.iloc[:, 29:33]

    df1 = pd.read_csv('../../data/house_belonging.csv')
    df0 = df1.groupby('belonging').count()
    df0 = df0.iloc[:, :1]
    df0.rename(columns={'Unnamed: 0': 'house_cnt'}, inplace=True)

    df1 = pd.read_csv('../../data/house_belonging.csv')
    df1 = df1.join(df3)
    df1 = df1.groupby('belonging').mean()
    df1 = df1.iloc[:, 1:]
    df1.info()

    df1 = pd.merge(df1, df0, on='belonging', how='outer')
    df1.to_csv('../../data/district1.csv')

    df2 = pd.read_csv('../../data/mall_belonging.csv')
    df2 = df2.groupby('belonging').count()
    df2 = df2.iloc[:, :1]
    df2.rename(columns={'Unnamed: 0': 'mall_cnt'}, inplace=True)
    df2.info()
    df2.to_csv('../../data/district2.csv')

    df1 = pd.read_csv('../../data/district1.csv')
    df2 = pd.read_csv('../../data/district2.csv')
    df_merged = pd.merge(df1, df2, on='belonging', how='outer')
    df_merged = df_merged.dropna(subset=['house_cnt'])
    df_merged['mall_cnt'] = df_merged['mall_cnt'].fillna(0)
    df_merged.info()
    df_merged.to_csv('../../data/district.csv', index=False)
