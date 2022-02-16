#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_link.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-16 14:08:53
    __Author__ = 黎晟
"""

import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='点击xxxx')
def test_with_named_link():
    pass


@allure.issue('140', 'bug的链接')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试用例的链接')
def test_with_testcase_link():
    pass
