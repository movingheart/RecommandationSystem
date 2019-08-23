"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-22 上午9:08
"""
import math
from operator import itemgetter

import sys
sys.path.append('.')
from utils.common import group_data
from data.read_data import ratings
from experiment import SplitData


def ItemSimilarity(train):
    # calculate co-rated users between items
    C = dict()
    N = dict()
    for u, items in train.items():
        for i in items:
            if i not in N:
                N[i] = 0
            N[i] += 1
            C[i] = dict()
            for j in items:
                if i==j:
                    continue
                if j not in C[i]:
                    C[i][j] = 0
                C[i][j] += 1

    # calculate finial similarity matrix W
    W = dict()
    for i, related_items in C.items():
        W[i] = dict()
        for j, cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W


def Recommendation(train, user_id, W, K, L):
    rank = dict()
    ru = train[user_id]
    for i in ru:
        pi = 1
        for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[:K]:
            if j in ru:
                continue
            if j not in rank:
                rank[j] = 0
            rank[j] += pi * wj
    return sorted(rank.items(), key=itemgetter(1), reverse=True)[:L]


if __name__ == "__main__":
    data = ratings[['UserID', 'MovieID']].values
    train_data, test_data = SplitData(data, 8, 5, 0)
    train = group_data(train_data)

    w = ItemSimilarity(train)
    print(Recommendation(train, 5, w, 8, 8))
