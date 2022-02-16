#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_step.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-12 18:52:13
    __Author__ = 黎晟
"""

import allure

from .steps import imported_step


@allure.step("step-1")
def passing_step():
    pass


@allure.step("step-2")
def step_with_nested_steps():
    nested_step()


@allure.step("step-3")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("step-4")
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_imported_step():
    passing_step()
    imported_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
