import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    corr = df.corr(method='pearson')
    columns_to_drop = [ 'Lng', 'Lat', 'Cid', 'followers', 'livingRoom', 'drawingRoom', 'kitchen', 'bathRoom', 'renovationCondition'
                       , 'ladderRatio', 'fiveYearsProperty', 'district', 'month', 'day', 'house_cnt', 'mall_cnt']
    corr = corr.drop(columns=columns_to_drop)
    rows_to_drop = [ 'Lng', 'Lat', 'Cid', 'followers', 'livingRoom', 'drawingRoom', 'kitchen', 'bathRoom', 'renovationCondition'
                   , 'ladderRatio', 'fiveYearsProperty', 'district', 'month', 'day', 'house_cnt', 'mall_cnt']
    
    corr = corr.drop(index=rows_to_drop)
    corr.to_csv('../../data/Corr_selected.csv')
