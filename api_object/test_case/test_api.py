# Time: 2021/4/27 17:29
# Author: jiangzhw
# FileName: test_api.py

from api_object.api import api


class TestApi:
    """test api case"""
    api = api.API()

    def test_get_token_bak(self):
        res = self.api.get_token()
        print("res", res)
        assert res["errcode"] == 0
