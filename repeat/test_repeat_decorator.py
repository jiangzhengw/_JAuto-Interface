#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_repeat_decorator.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-03-02 17:18:01
    __Author__ = 黎晟
"""

import pytest


@pytest.mark.repeat(3)
def test_repeat_decorator():
    pass
