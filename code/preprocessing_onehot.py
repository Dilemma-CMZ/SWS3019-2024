import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('../data/BeijingHousingPrices_preprocessed.csv')
    one_hot_encoded_df = pd.get_dummies(df['buildingType'])
    df = df.join(one_hot_encoded_df)
    df.info()
    df.rename(columns={df.columns[28]: 'buildingType_towel'}, inplace=True)
    df.rename(columns={df.columns[29]: 'buildingType_bungalow'}, inplace=True)
    df.rename(columns={df.columns[30]: 'buildingType_comb'}, inplace=True)
    df.rename(columns={df.columns[31]: 'buildingType_plate'}, inplace=True)
    df.to_csv('../data/BJ1.csv')
