#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_dynamic2.py.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-26 18:24:36
    __Author__ = 黎晟
"""
import allure


def test_other_with_dynamic():
    assert 1 == 1
    allure.dynamic.feature('动态feature')
    allure.dynamic.story('动态story')
    allure.dynamic.severity(allure.severity_level.BLOCKER)
    allure.dynamic.link("dynamic动态生成的Link:https://blog.csdn.net/qq_42841075?type=blog")
    allure.dynamic.issue("dynamic动态生成的Issue:https://blog.csdn.net/qq_42841075?type=blog")
    allure.dynamic.testcase("dynamic动态生成的testcase:https://blog.csdn.net/qq_42841075?type=blog", "dynamic动态生成的testcase")

#
# data_dynamic = [
#     ("name1", "password1", "登录成功用例"),
#     ("name2", "password2", "登录失败用例"),
#     ("name3", "password3", "账号不存在用例")
# ]
#
#
# @pytest.mark.parametrize("name,pwd,title", data_dynamic)
# def test_with_dynamic(name, pwd, title):
#     """
#      登录用例
#     """
#     allure.dynamic.title(title)
#     allure.dynamic.description(f'nam为{name},pwd为{pwd}')
