"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-17 下午5:51
"""
from operator import itemgetter
import math
import sys
sys.path.append('.')
from utils.common import group_data, print_run_time
from data.read_data import ratings
from experiment import SplitData


def UserSimilarity1(train):
    """ 时间复杂度n*n

    :param train:
    :return:
    """
    W = dict()
    for u in train.keys():
        W[u] = dict()
        for v in train.keys():
            if u == v:
                continue
            W[u][v] = len(train[u] & train[v])
            W[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return W


def UserSimilarity(train):
    """ 改进的计算方法

    :param train:
    :return:
    """
    # build inverse table for item_users
    item_users = dict()
    for u, items in train.items():
        for i in items:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # calculate co-related items between users
    C = dict()  # 用户之间的相似物品数
    N = dict()  # 每个用户的物品数
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 0
            N[u] += 1
            C[u] = dict()
            for v in users:
                if u == v:
                    continue
                if v not in C[u]:
                    C[u][v] = 0
                C[u][v] += 1

    # calculate finnial similarity matrix W
    W = dict()
    for u, related_users in C.items():
        W[u] = dict()
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])

    return W


def Recommend(user, train, W, K, L):
    rank = dict()
    # 获得用户user看过的商品
    interacted_items = train[user]
    # 得到和用户user兴趣最接近的K个用户
    for v, wuv in sorted(W[user].items(), key=itemgetter(1), reverse=True)[0:K]:
        # 处理用户v看过的商品i
        for i in train[v]:
            rvi = 1
            if i in interacted_items:
                continue
            if i not in rank:
                rank[i] = 0
            rank[i] += wuv * rvi
    return sorted(rank.items(), key=itemgetter(1), reverse=True)[:L]

if __name__ == "__main__":
    data = ratings[['UserID', 'MovieID']].values
    train_data, test_data = SplitData(data, 8, 2, 0)
    train = group_data(train_data)
    w = UserSimilarity1(train)
    print(Recommend(4, train, w, 8, 8))
    print(Recommend(4004, train, w, 8, 8))
    print(Recommend(1958, train, w, 8, 8))
    print(Recommend(1962, train, w, 8, 8))