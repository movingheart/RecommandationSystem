"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-3 下午7:46
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def gen_data():
    """ 造数据

    :return:
    """
    # 所有商品（假设10个）的被推荐次数
    total = 1000

    # 每个商品被推荐的次数
    data = [5, 18, 12, 45, 34, 26, 17, 27, 206, 610]

    # 每个商品的流行度
    p = [x/total for x in data]

    # 为便于计算，载入dataframe
    df = pd.DataFrame({'num': data, 'prob': p})
    # print(df)
    return df


def plot_gini(my_df):
    plt.figure()
    my_df['num_cumsum'] = [i/10 for i in range(1,11)]
    my_df.sort_values(by='prob')
    my_df['cumsum'] = my_df['prob'].cumsum()
    my_df.plot(x='num_cumsum', y='cumsum', color='blue')


    plt.plot(my_df.loc[[0,9],['num_cumsum']]['num_cumsum'],
             my_df.loc[[0, 9], ['cumsum']]['cumsum'],
             color='r')

    plt.fill(my_df['num_cumsum'], my_df['cumsum'], color='grey')
    plt.fill_between(my_df['num_cumsum'], my_df['cumsum'], color='green')
    plt.xlabel("商品个数累计占比")
    plt.ylabel("流行度数累计占比")
    plt.text(0.7, 0.4, "A", fontdict={'size': 16, 'color': 'r'})
    plt.text(0.9, 0.1, "B", fontdict={'size': 16, 'color': 'r'})
    plt.show()
    print(my_df)

if __name__ == "__main__":
    df = gen_data()
    plot_gini(df)
