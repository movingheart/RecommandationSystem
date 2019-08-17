"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-16 上午8:41
Note: 以下每个函数要求的数据结构不一样，大家在看的时候，单独看每个函数意义即可
"""
import random
import math
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


def Coverage(train, test, N):
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for item in train[user]:
            all_items.add(item)
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            recommend_items.add(item)
    return len(recommend_items) / len(all_items) * 1.0


def Popularity(train, test, N):
    # 训练集中每个物品出现的次数, 即出现在了多少个用户中
    item_popularity = dict()
    for user, items in train.items():
        for item in items:
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1
    # 物品在训练集中出现的次数
    ret = 0
    # 所有商品在推荐列表中出现的总次数
    n = 0
    for user in train.keys():
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            ret += math.log(1 + item_popularity.get(item, 0))
            n += 1
    # 物品出现的次数 除以 总的物品数
    ret /= n*1.0
    return ret

if __name__ == "__main__":
    # 测试SplitData
    data = ratings[['UserID','MovieID']].values

    train_data, test_data = SplitData(data, 8, 1, 0)

    print("训练数据：", train_data[:2], "\n测试数据：", test_data[:2])


    def group_data(d):
        """给数据分组，形成字典：key为用户id，value为item集合

        :param d:二维列表
        :return:
        """
        dic = dict()
        for a, b in groupby(d, key=lambda e:e[0]):
            dic[a] = set([i[1] for i in b])
        return dic


    # 测试Recall
    train = group_data(train_data)
    test = group_data(test_data)
    print("召回率：", Recall(train, test, 8))

    # 测试Precision
    print("准确率：", Precision(train, test, 8))

    # 测试覆盖率
    print("覆盖率：", Coverage(train, test, 8))

    # 流行度
    print("流行度：", Popularity(train, test, 8))
