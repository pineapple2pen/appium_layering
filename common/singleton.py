# -*- coding: utf-8 -*-
# @Author : Pineapple Dong ^_^
# @Time   : 2018/4/17 20:28
# @File   : singleton.py
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
