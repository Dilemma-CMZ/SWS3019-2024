import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    df = df[['subway', 'mall_cnt']]
    # df = df[df['mall_cnt'] >= 13]
    # df = df[df['mall_cnt'] <= 16]
    # df = df[df['subway'] >= 0.8]
    # df = df[df['subway'] <= 1.0]
    df.info()

    plt.scatter(df['subway'], df['mall_cnt'])

    plt.title('')
    plt.xlabel('Subway')
    plt.ylabel('Number of Mall')

    plt.show()
