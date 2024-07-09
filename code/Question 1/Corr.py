import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('district.csv')
    corr = df.corr(method='pearson')
    corr = corr['mall_cnt']
    print(corr)
    corr.to_csv('Corr_mall.csv')

