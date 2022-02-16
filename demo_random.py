#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = demo_random.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-16 17:06:46
    __Author__ = 黎晟
"""
import random

# 先定义一个目标子串
import string

GRAMMAR = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"


def random_str(length):
    """生成随机长度str"""
    target = ""
    grammar_length = len(GRAMMAR) - 1
    if length > 0:
        for i in range(length):
            # tmp_str = random.choice(GRAMMAR)
            tmp_str = GRAMMAR[random.randint(0, grammar_length)]
            target += tmp_str
        return target
    else:
        raise IndexError()


def random_str_gds(length):
    return ''.join([random.choice(string.digits + string.ascii_letters) for i in range(length)])


def random_str_gds_detail(length):
    target_lst = []
    for i in range(length):
        grammar = string.digits + string.ascii_letters
        target_lst.append(random.choice(grammar))
    return ''.join(target_lst)


# 测试用例
print("用例1：", random_str(10))
# print("用例2：", random_str(0))
print("用例1：", random_str_gds(10))
print("用例1：", random_str_gds_detail(10))
