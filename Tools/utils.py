# coding: utf-8

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
