"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-17 下午5:57
"""
import time
from itertools import groupby

def group_data(d):
    """给数据分组，形成字典：key为用户id，value为item集合

    :param d:二维列表
    :return:
    """
    dic = dict()
    for a, b in groupby(d, key=lambda e: e[0]):
        dic[a] = set([i[1] for i in b])
    return dic



def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('Current Function [%s] spend time: %.2f' % (func.__name__ ,time.time() - local_time))
    return wrapper
