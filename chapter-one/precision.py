import math
import random


# 所有商品编号
ITEMS = random.sample(range(1, 10000), 1000)
# 所有用户编号
USERS = random.sample(range(1, 1000), 100)


def get_data():
    """ 造数

    :return:
    """
    res = []
    user_count = 5
    item_count = 10

    for i in range(item_count):
        u = random.randint(1, user_count)
        rui = random.randint(1, 5)
        pui = random.randint(1, 5)
        res.append((u, i, rui, pui))
    return res


def RMSE(records):
    return math.sqrt(
        sum([(rui - pui) * (rui - pui) for u, i, rui, pui in records]) / float(len(records))
    )


def MAE(records):
    return sum([abs(rui-pui) for u, i, rui, pui in records]) / float(len(records))


def Recommand(user, n):
    """ 给用户推荐n个商品

    :param user: 用户id
    :param n: 商品个数
    :return: 商品列表
    """
    return set(random.sample(ITEMS, n))


def PrecisionRecell(test, N):
    hit = 0
    n_recall = 0
    n_precision = 0
    for user, items in test.items():
        rank = Recommand(user, N)
        hit += len(rank & items)
        n_recall += len(items)
        n_precision += N
    return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]


if __name__ == "__main__":
    rs = get_data()
    print("RMSE:", RMSE(rs))
    print("MAE:", MAE(rs))

    N = 8  # 推荐个数 top 8
    test_data = {user: set(random.sample(ITEMS, 20)) for user in USERS}   # 用户产生过行为的商品个数为20
    result = PrecisionRecell(test_data, N)
    print("准确率：{}，召回率：{}".format(result[0], result[1]))
