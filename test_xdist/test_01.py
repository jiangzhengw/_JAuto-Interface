#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_01.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-28 15:17:11
    __Author__ = 黎晟
"""
from time import sleep

import pytest


@pytest.mark.parametrize("x", list(range(10)))
def test_index(pwd_login, x):
    sleep(1)
    print("首页用例", x)
