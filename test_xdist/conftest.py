#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = conftest_tmp.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-28 15:17:17
    __Author__ = 黎晟
"""
import pytest


@pytest.fixture(scope="session")
def pwd_login():
    print("== 开始用例 ==")
    name, pwd = "admin", "123456"
    yield name, pwd
    print("== 退出用例 ==")
