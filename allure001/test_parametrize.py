#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = test_parametrize.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-25 15:00:09
    __Author__ = 黎晟
"""
import allure
import pytest

data1 = [
    pytest.param(1, id="id标记：测试用例1"),
    pytest.param(2, id="id标记：测试用例1"),
    pytest.param(3, id="id标记：测试用例1")
]

data2 = [
    pytest.param({"username": "name1", "pwd": "pwd1"}, id="name1登录成功"),
    pytest.param({"username": "name2", "pwd": "pwd2"}, id="name2登录成功"),
    pytest.param({"username": "name3", "pwd": "pwd3"}, id="name3登录失败")
]


@pytest.fixture()
def login(request):
    """登录fixture"""
    param = request.param
    print(f"账号是：{param['username']}，密码是：{param['pwd']}")
    # 返回
    return {"code": 0, "msg": "success!"}


# 参数化默认的标题
# @pytest.mark.parametrize("login", data_login, indirect=True)
# def test_parametrize_without_title(login):
#     assert login['code'] == 0


# 参数化使用id
# @pytest.mark.parametrize("login", data_login, indirect=True)
# def test_parametrize_without_id(login):
#     assert login['code'] == 0

# 参数化+allure.title()写死标题
# @allure.title("登录测试用例：name1成功，name2失败，name3用户名不存在")
# @pytest.mark.parametrize("login", data_login, indirect=True)
# def test_parametrize_without_id(login):
#     assert login['code'] == 0


# login_ids = ["name1登录成功", "name2登录失败", "name3用户名不存在"]

# 参数化使用ids
# @pytest.mark.parametrize("login", data_login, ids=login_ids, indirect=True)
# def test_parametrize_without_id(login):
#     assert login['code'] == 0


data_login_with_fixture = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
    {"username": "name3", "pwd": "pwd3"}
]


# 参数化+allure.title()动态生成标题,结合fixture
@allure.story("结合fixture")
@allure.title("登录用例-{login}")
@pytest.mark.parametrize("login", data_login_with_fixture, indirect=True)
def test_parametrize_without_id1(login):
    assert login['code'] == 0


data_login_without_fixture = [
    ("name1", "123456", "name1 登录成功"),
    ("name2", "123456", "name2 登录失败"),
    ("name3", "123456", "name3 账号不存在")
]


# 参数化+allure.title()动态生成标题,不结合fixture
@allure.story("不结合fixture")
@allure.title("登录-{title}")
@pytest.mark.parametrize("username,pwd,title", data_login_without_fixture)
def test_parametrize_without_id2(username, pwd, title):
    print(username, pwd)
