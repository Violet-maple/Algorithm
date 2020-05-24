# coding: utf-8

import inspect


def get_function_name():
    """
    获取当前函数名
    :return: str
    """
    return inspect.stack()[1][3]


def get_function_info():
    return inspect.stack()[1][1]
