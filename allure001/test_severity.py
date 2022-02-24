#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_severity.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-18 19:53:57
    __Author__ = 黎晟
"""
import allure


def test_with_no_severity_label():
    """ 没标记 severity 的方法默认优先级为 normal"""
    assert 1 == 2


@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity():
    """优先级为 blocker"""
    assert 1 == 2


@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    """优先级为 critical"""
    assert 1 == 2


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    """优先级 normal"""
    assert 1 == 2


@allure.severity(allure.severity_level.MINOR)
def test_with_minor_severity():
    """优先级为 minor"""
    assert 1 == 2


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    """方法优先级为 trivial"""
    assert 1 == 2


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    """类优先级 NORMAL"""

    def test_inside_the_normal_severity_test_class(self):
        """默认集成类优先级 NORMAL"""
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        """类优先级 normal，函数优先级 critical"""
        pass