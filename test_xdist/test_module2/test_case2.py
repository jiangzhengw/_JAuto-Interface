#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_case2.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-28 15:28:08
    __Author__ = 黎晟
"""
from time import sleep

import pytest


@pytest.mark.parametrize("x", list(range(10)))
def test_func1(x):
    sleep(1)
    print("module2 测试用例-2", x)
