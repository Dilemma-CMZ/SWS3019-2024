import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    corr = df.corr(method='pearson')
    # corr = corr['mall_cnt']
    print(corr)
    corr.to_csv('../../data/Corr_mall.csv')
