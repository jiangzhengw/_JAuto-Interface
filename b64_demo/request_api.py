# Time: 2021/4/14 19:33
# Author: jiangzhw
# FileName: request_api.py
import json

import requests
import base64


class RequestApi:

    def send(self, data: dict):
        print(data)
        res = requests.request(data["method"], url=data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.text))
        elif data["encoding"] == "others":
            # 可以将返回值发送给三方服务，让三方去解密，然后拿到解密内容
            return json.loads(requests.post("三方解密url", data=res.text).text)
        else:
            return res.text
