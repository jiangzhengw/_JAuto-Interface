#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_title.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-15 19:37:59
    __Author__ = 黎晟
"""

import allure
import pytest


@allure.title("自定义的标题")
def test_with_a_title():
    assert 2 + 2 == 4


@allure.title("此测试有一个带有 unicode 的自定义标题：Привет！")
def test_with_unicode_title():
    assert 3 + 3 == 6


@allure.title("前置操作的标题")
@pytest.fixture()
def front_fixture(request):
    params = request.param
    name = params["username"]
    pwd = params["pwd"]
    print(name, pwd, params)


@allure.title("结合参数化使用的标题: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected
