# coding: utf-8

import inspect


def get_function_name():
    return inspect.stack()[1][3]
