#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_case1.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-28 15:18:08
    __Author__ = 黎晟
"""
from time import sleep

import pytest


@pytest.mark.parametrize("x", list(range(10)))
def test_func1(x):
    sleep(1)
    print("module1 测试用例-1", x)
