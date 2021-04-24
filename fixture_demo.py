# Time: 2021/4/24 14:14
# Author: jiangzhw
# FileName: fixture_demo.py
import pytest

# 多参数多值
user_data = [
    ("name1", 123456),
    ("name2", 123456)
]


@pytest.mark.parametrize("user,pwd", user_data)
def test(user, pwd):
    print(user, pwd)


data = ["name1", "name2"]
user_pwd_data = [
    {"user": "admin1", "psw": 123456},
    {"user": "admin2", "psw": 654321}
]


@pytest.fixture(scope="module")
def login1(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.fixture(scope="module")
def login2(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    return user, psw


# 1、@pytest.mark.parametrize('login',params)
# 2、@pytest.mark.parametrize('login',params,indirect=True)
# 当引用1的时候，login就理解成一个变量，执行后的结果就是login=[{'user':'admin','pwd':''}],
#
# 当使用2的时候，login变为一个可执行的函数，再将params当参数传入login函数中去执行，当其他变量被赋值为login的时候
@pytest.mark.parametrize("login1", data, indirect=True)
def test_login1(login1):
    """登录用例"""
    a = login1
    print("测试用例中login的返回值:%s" % a)
    assert a != ""


@pytest.mark.parametrize("login2", user_pwd_data, indirect=True)
def test_login1(login2):
    """登录用例"""
    user = login2[0]
    psw = login2[1]
    assert user != ""
    assert psw != ""


# 多个fixture
user = []
psw = []


@pytest.fixture(scope="module")
def input_user(request):
    pass


@pytest.fixture(scope="module")
def input_psw(request):
    pass


@pytest.mark.parametrize("input_user", user, indirect=True)
@pytest.mark.parametrize("input_psw", psw, indirect=True)
def test_login(input_user, input_psw):
    """登录用例"""
    a = input_user
    b = input_psw
    print("测试数据a-> %s， b-> %s" % (a, b))
    assert b
