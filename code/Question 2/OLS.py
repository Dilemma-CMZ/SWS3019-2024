import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../data/district.csv')
    df = df[['subway', 'mall_cnt']]
    df = df[df['mall_cnt'] >= 10]
    df = df[df['mall_cnt'] <= 20]
    len = df.shape[0]
    print(len)

    print("0 - 0.2")
    df1 = df[df['subway'] >= 0]
    df1 = df1[df1['subway'] <= 0.2]
    print(df1.shape[0] / len)

    print("0.2 - 0.4")
    df2 = df[df['subway'] >= 0.2]
    df2 = df2[df2['subway'] <= 0.4]
    print(df2.shape[0] / len)

    print("0.4 - 0.6")
    df3 = df[df['subway'] >= 0.4]
    df3 = df3[df3['subway'] <= 0.6]
    print(df3.shape[0] / len)

    print("0.6 - 0.8")
    df4 = df[df['subway'] >= 0.6]
    df4 = df4[df4['subway'] <= 0.8]
    print(df4.shape[0] / len)

    print("0.8 - 1.0")
    df5 = df[df['subway'] >= 0.8]
    df5 = df5[df5['subway'] <= 1.0]
    print(df5.shape[0] / len)

    # plt.scatter(df['subway'], df['mall_cnt'])
    #
    # plt.title('')
    # plt.xlabel('Subway')
    # plt.ylabel('Number of Mall')
    #
    # plt.show()
