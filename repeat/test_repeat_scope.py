#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_repeat_scope.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-03-02 17:23:16
    __Author__ = 黎晟
"""


class TestScope1:
    def test_repeat_scope1(self):
        print("测试用例执行1")


class TestTestScope2:
    def test_repeat_scope2(self):
        print("测试用例执行2")


def test_outside1():
    print("执行class外用例1")


def test_outside2():
    print("执行class外用例2")
