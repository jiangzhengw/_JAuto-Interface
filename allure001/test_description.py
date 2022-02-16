#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_description.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-15 18:37:36
    __Author__ = 黎晟
"""
import allure


@allure.description_html("""
<h1>测试用例的一些HTML描述</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr align="center">
    <td>William</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr align="center">
    <td>Vasya</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
""")
def test_html_description():
    assert True


@allure.description("""
多行测试说明
使用 allure.description 装饰器.
没什么特别的地方
""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)


def test_unicode_in_docstring_description():
    """Unicode 描述.
    Этот тест проверяет юникод.
    你好伙计.
    """
    assert 42 == int(6 * 7)


@allure.description("""
用例开始描述：将在测试用例结束被替换
""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('用例结束描述.')
