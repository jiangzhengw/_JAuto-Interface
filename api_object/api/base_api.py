# Time: 2021/4/27 17:56
# Author: jiangzhw
# FileName: base_api.py
import requests


class BaseApi:
    """base api"""

    def requests_http(self, req):
        res = requests.request(**req)
        return res.json()
