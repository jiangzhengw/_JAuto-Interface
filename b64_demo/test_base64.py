# Time: 2021/4/14 19:16
# Author: jiangzhw
# FileName: test_base64.py
import json

import requests
import base64
from b64_demo import request_api


class TestBase64:
    # python -m http.server 8888 起一个本地服务
    def setup_method(self):
        self.ra = request_api.RequestApi()

    def test_decode(self):
        """
        测试解码
        :return:
        """
        url = "http://127.0.0.1:8888/demo1.txt"
        res = requests.get(url=url)
        res = base64.b64decode(res.text)
        print(json.loads(res))

    def test_encode(self):
        """
        测试编码
        :return:
        """
        url = "http://127.0.0.1:8888/demo2.json"
        res = requests.get(url=url)
        res = base64.b64encode(res.text.encode('utf-8')).decode("ascii")
        print(res)

    def test_test_decode_bak(self):
        req_data = {
            "method": "get",
            "url": "http://127.0.0.1:8888/demo1.txt",
            "headers": None,
            "encoding": "base64"
        }
        print(self.ra.send(req_data))
