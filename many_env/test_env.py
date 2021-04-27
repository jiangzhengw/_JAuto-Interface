# Time: 2021/4/21 20:17
# Author: jiangzhw
# FileName: test_env.py
from many_env.env_api import EnvApi


class TestEnv:
    api = EnvApi()

    def test_send(self):
        data = {
            "method": "get",
            "url": f"http://host:8888/demo1.txt",
            "headers": None
        }
        res = self.api.send(data)
        print(res.text)
