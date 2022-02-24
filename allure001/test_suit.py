#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_suit.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-23 11:39:25
    __Author__ = 黎晟
"""
import allure


@allure.suite("测试套件 suite")
def test_suite1():
    pass


@allure.parent_suite("测试套件 parent_suite")
def test_suite3():
    pass


@allure.sub_suite("测试套件 sub_suite")
def test_suite4():
    pass


@allure.suite("测试类套件")
class TestSuite1:

    @allure.suite("类内部测试套件1")
    def test_inside_suite1(self):
        """内部测试套件1"""
        pass

    def test_inside_without_suite1(self):
        pass


class TestSuite2:
    """无suite修饰的测试类"""

    @allure.suite("类内部测试套件2")
    def test_inside_suite3(self):
        pass

    def test_inside_without_suite2(self):
        pass
