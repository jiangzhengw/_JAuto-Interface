#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __File__   = conftest.py
    __Project__= _JAuto-Interface
    __Time__   = 2022-02-28 21:09:02
    __Author__ = 黎晟
"""
import json
from random import random

import pytest
from filelock import FileLock


# 不使用文件锁
# @pytest.fixture(scope="session")
# def xdist_fixture():
#     data = str(random())
#     return data


# 使用文件锁
@pytest.fixture(scope="session")
def xdist_fixture(tmp_path_factory, worker_id):
    # 如果是单机运行 则运行这里的代码块【不可删除、修改】
    if worker_id == "master":
        """
        【自定义代码块】
        这里就写你要本身应该要做的操作，比如：登录请求、新增数据、清空数据库历史数据等等
        """
        data = str(random())
        # 如果测试用例有需要，可以返回对应的数据，比如 token
        print(f"master首次执行，数据是{data} ")
        return data
    # 如果是分布式运行
    # 获取所有子节点共享的临时目录，无需修改【不可删除、修改】
    root_tmp_dir = tmp_path_factory.getbasetemp().parent
    # 【不可删除、修改】
    fn = root_tmp_dir / "data.json"
    # 【不可删除、修改】
    with FileLock(str(fn) + ".lock"):
        # 【不可删除、修改】
        if fn.is_file():
            # 缓存文件中读取数据，像登录操作的话就是token 【不可删除、修改】
            data = json.loads(fn.read_text())
            print(f"worker读取缓存文件，数据是{data} ")
        else:
            """
            【自定义代码块】
            这里就写你要本身应该要做的操作，比如：登录请求、新增数据、清空数据库历史数据等等
            """
            data = str(random())
            # 【不可删除、修改】
            fn.write_text(json.dumps(data))
            print(f"worker首次执行，数据是{data} ")
            # 如果测试用例有需要，可以返回对应的数据，比如 token
    return data
