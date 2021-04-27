# Time: 2021/4/27 17:29
# Author: jiangzhw
# FileName: api.py
import json
from string import Template

import yaml

from api_object.api.base_api import BaseApi

_corpid = 'wwa2fcd79577974bd3'
_corpsecret = '6KMV_5vrtuiyeaaJf66xsxndsHat_M_Xcw2ygIaZ-to'


class API(BaseApi):
    """api"""

    def get_token(self):
        """get_token method"""
        # req = {
        #     "method": "get",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     "params": {
        #         "corpid": _corpid,
        #         "corpsecret": _corpsecret
        #     }
        # }
        # yaml无参数替换
        # req = yaml.safe_load(open("../api/get_token.yml"))

        req = self.replace()
        res = self.requests_http(req)
        return json.loads(res.text)

    def replace(self):
        """替换yaml文件方法"""
        # TODO :应该放到 BasePage http(方法内)
        print(_corpid, _corpsecret)
        params = {
            "corpid": _corpid,
            "corpsecret": _corpsecret
        }
        with open("../api/get_token.yml") as f:
            print("替换前：", f.read(), "类型：", type(f.read()))
            s = Template(f.read())
            raw = s.substitute(corpid=_corpid, corpsecret=_corpsecret)
            # raw = Template(f.read()).substitute(params)
            # TODO : 替换后为空待解决
            print("替换后：", raw, "type:", type(raw))
            # 将字符串转为python对象
        return yaml.safe_load(raw)

    def to_taml(self):
        # 打开一个文件（如果没有则创建），将数据存成yaml的形式
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "$corpid",
                "corpsecret": "$corpsecret"
            }
        }
        with open("get_token.yml", "w") as f:
            yaml.safe_dump(data, stream=f)


if __name__ == "__main__":
    api = API()
    api.replace()
