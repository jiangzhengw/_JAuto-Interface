#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_tags.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-17 17:49:03
    __Author__ = 黎晟
"""

import allure


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.story('epic_1')
def test_with_epic_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass


@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass


@allure.epic('epic_2')
@allure.feature('feature_2')
@allure.story('story_2')
def test_with_epic_2_story_2_and_feature_2():
    pass
