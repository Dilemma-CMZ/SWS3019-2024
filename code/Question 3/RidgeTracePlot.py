import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    X = df[['communityAverage', 'floor_num', 'house_cnt', 'elevator']]
    y = df[['mall_cnt']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler_X = StandardScaler()
    X_train_scaled = scaler_X.fit_transform(X_train)
    X_test_scaled = scaler_X.transform(X_test)

    alphas = np.logspace(-4, 4, 50)

    coefficients = []

    for alpha in alphas:
        ridge = Ridge(alpha=alpha)
        ridge.fit(X_train_scaled, y_train)
        coefficients.append(ridge.coef_.ravel())

    coefficients = np.array(coefficients)

    arr = np.array(coefficients)
    df = pd.DataFrame({'alphas': alphas, 'coe1': arr[:, 0], 'coe2': arr[:, 1], 'coe3': arr[:, 2],
                       'coe4': arr[:, 3]})
    print(df)
    df.to_csv('../../data/RidgeTrace.csv')

    plt.figure(figsize=(10, 8))
    for i in range(X.shape[1]):
        plt.plot(alphas, coefficients[:, i], label=f'Feature {i}')

    plt.xlabel('Regularization parameter alpha')
    plt.ylabel('Coefficient values')
    plt.title('Ridge Trace')
    plt.legend()
    plt.xscale('log')
    plt.show()
