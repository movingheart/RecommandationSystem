"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-16 上午8:41
Note: 以下每个函数要求的数据结构不一样，大家在看的时候，单独看每个函数意义即可
"""
import random
from itertools import groupby
import sys
sys.path.append('.')
from utils.recommend import GetRecommendation
from data.read_data import ratings


def SplitData(data, M, k, seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        # 注意：由于random.randint(0,M)的取值范围是[0,M]，这里取M-1
        if random.randint(0, M-1) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test


def Recall(train, test, N):
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test:
            continue
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)

    return hit / (all * 1.0)


def Precision(train, test, N):
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test:
            continue
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += N
    return hit / (all * 1.0)


if __name__ == "__main__":
    # 测试SplitData
    data = ratings[['UserID','MovieID']].values

    train_data, test_data = SplitData(data, 8, 1, 0)

    print("训练数据：", train_data[:2], "\n测试数据：", test_data[:2])

    # 测试Recall
    def group_data(d):
        dic = dict()
        for a, b in groupby(d, key=lambda e:e[0]):
            dic[a] = set([i[0] for i in b])
        return dic

    train = group_data(train_data)
    test = group_data(test_data)
    print("召回率：", Recall(train, test, 8))

    # 测试Precision
    print("准确率：", Precision(train, test, 8))