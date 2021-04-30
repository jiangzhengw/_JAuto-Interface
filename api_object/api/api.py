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

    def get_token(self, secret=None):
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
        if secret is None:
            req = self.replace()
        else:
            req = {
                "method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {
                    "corpid": _corpid
                }
            }
            req['params']['corpsecret'] = secret
        res = self.requests_http(req)
        return res

    def replace(self):
        """替换yaml文件方法"""
        # TODO :应该放到 BasePage http方法内
        params = {
            "corpid": _corpid,
            "corpsecret": _corpsecret
        }

        # substitute 和 safe_substitute 区别，详细见官方文档
        with open("../api/get_token.yml", encoding="utf-8") as f:
            # print("替换前：", f.read(), "类型：", type(f.read()))
            # down : 替换后为空待解决(将读取的文件存到变量内)
            # 真正原因：f.read()方法，第一次读取后，如果不执行f.close()操作，后续的同一文件读取都是从文件末尾进行读取，因此读取的内容为空
            # read_yml = f.read()
            # raw = Template(read_yml).substitute(corpid=_corpid, corpsecret=_corpsecret)
            # raw = Template(read_yml).substitute(params)
            raw = Template(f.read()).safe_substitute(params)
            print("替换后：", raw, "type:", type(raw))
        # 将字符串转为python对象
        return yaml.safe_load(raw)


if __name__ == "__main__":
    api = API()
    api.replace()
