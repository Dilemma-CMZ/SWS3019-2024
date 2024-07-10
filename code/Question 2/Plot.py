import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = pd.DataFrame({
        'Subway': ['0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0'],
        '5-8': [2, 3, 6, 1, 9],
        '9-12': [0, 0, 0, 1, 2],
        '13-16': [0, 0, 3, 2, 1]
    })

    categories = df['Subway']
    N = len(categories)
    ind = np.arange(N)

    width = 0.15
    plt.bar(ind, df['5-8'], width, label='5-8')
    plt.bar(ind + width, df['9-12'], width, label='9-12')
    plt.bar(ind + 2 * width, df['13-16'], width, label='13-16')

    plt.xticks(ind + width, categories)

    plt.legend()

    plt.title('Subway & Number of Mall')
    plt.xlabel('Subway')
    plt.ylabel('Number of Mall')

    plt.show()
