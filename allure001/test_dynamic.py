#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_dynamic.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-16 11:26:39
    __Author__ = 黎晟
"""
import allure
import pytest

data = [
    ("测试用例初始描述-1", "测试用例后描述-1"),
    ("测试用例初始描述-2", "测试用例后描述-2"),
    ("测试用例初始描述-3", "测试用例后描述-3")
]


@pytest.mark.parametrize("description_front,description_final", data)
def test_no_dynamic_description(description_front):
    """
    结合参数化描述：{description_front}
    """
    # allure.dynamic.description(description_final)
    print("用例详情：test_no_dynamic_description")


@pytest.mark.parametrize("description_front,description_final", data)
def test_dynamic_description(description_front, description_final):
    """
    用例初始描述
    """
    allure.dynamic.description(description_final)
