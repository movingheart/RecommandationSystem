"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-16 上午8:52
"""
from data.read_data import movies


def GetRecommendation(user, N):
    items = movies['MovieID'].sample(N)
    return [(x, 1) for x in items]


if __name__ == "__main__":
    print(GetRecommendation('xiaoming', 8))