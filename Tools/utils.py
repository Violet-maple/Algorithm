# coding: utf-8

import time
import functools


def func_cache(func):
    """
    装饰器实例: 函数缓存
    :param func:
    :return:
    """
    cache = {}
    
    @functools.wraps(func)
    def _inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return _inner


def timer(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print(func.__name__, e - s)
        return result
    
    return _inner
