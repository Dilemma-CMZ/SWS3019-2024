import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    X = df[['communityAverage', 'floor_num', 'house_cnt', 'elevator']]
    y = df[['mall_cnt']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=37)

    scaler_X = StandardScaler()
    X_train_scaled = scaler_X.fit_transform(X_train)
    X_test_scaled = scaler_X.transform(X_test)

    ridge_reg = Ridge(alpha=5.0)

    ridge_reg.fit(X_train_scaled, y_train)

    y_pred = ridge_reg.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    r2 = r2_score(y_test, y_pred)
    print(f"R^2 Score: {r2}")
