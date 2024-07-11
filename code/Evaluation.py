import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    # question 3 parameters
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0

    df0 = pd.read_csv('../data/district.csv')
    df = pd.DataFrame()
    df['belonging'] = df0['belonging']
    df['mall_cnt'] = df0['mall_cnt']
    df['subway'] = df0['subway']
    scaler = StandardScaler()
    df['score2'] = scaler.fit_transform(df[['subway']])

    df['communityAverage'] = df0['communityAverage']
    df['floor_num'] = df0['floor_num']
    df['house_cnt'] = df0['house_cnt']
    df['elevator'] = df0['elevator']
    df['score3'] = w1 * df['communityAverage'] + w2 * df['floor_num'] + w3 * df['house_cnt'] + w4 * df['elevator']
    df['score3'] = scaler.fit_transform(df[['score3']])

    for y in range(2010, 2019):
        df1 = pd.read_csv('../data/district' + str(y) + '.csv')
        df1 = df1[['belonging', 'buildingType_towel', 'buildingType_comb', 'buildingType_plate', 'house_cnt']]
        df1.rename(columns={'buildingType_towel': 'buildingType_towel' + str(y)}, inplace=True)
        df1.rename(columns={'buildingType_comb': 'buildingType_comb' + str(y)}, inplace=True)
        df1.rename(columns={'buildingType_plate': 'buildingType_plate' + str(y)}, inplace=True)
        df1.rename(columns={'house_cnt': 'house_cnt' + str(y)}, inplace=True)
        df = pd.merge(df, df1, on='belonging', how='left')
        df = df.fillna(0)

    df.info()
    df.to_csv('../data/evaluation.csv')
