# Time: 2021/4/27 17:29
# Author: jiangzhw
# FileName: test_api.py
import pytest
import yaml

from api_object.api import api


class TestApi:
    """test api case"""
    api = api.API()

    def test_get_token_bak(self):
        res = self.api.get_token()
        print("res", res)
        assert res["errcode"] == 0

    @pytest.mark.parametrize("secret", yaml.safe_load(open("../api/secret.yml")))
    def test_get_token_bak2(self, secret):
        res = self.api.get_token(secret)
        print("res", res)
        assert res["errcode"] == 0
