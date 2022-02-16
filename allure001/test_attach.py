#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_attach.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-14 19:51:24
    __Author__ = 黎晟
"""
import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('在fixture前置步骤中添加一个txt附件', 'fixture 前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置步骤中添加一个txt附件', 'fixture 后置附件',
                      allure.attachment_type.TEXT)

    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attachments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass


def test_multiple_attachments():
    allure.attach.file('chestnut_1f330.png', attachment_type=allure.attachment_type.PNG)
    allure.attach.file('allure_report.html', attachment_type=allure.attachment_type.HTML)
    allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
