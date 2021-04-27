# Time: 2021/4/21 20:17
# Author: jiangzhw
# FileName: env_api.py
"""
在请求之前，对请求的url进行替换

- 二次封装requests，对请求进行定制化
- 将请求结构体的url进行参数化，从写死的ip地址改为一个任意的域名
- 使用一个env配置文件，存放各个环境的配置信息
- 将请求结构体中的url替换为env配置文件中的个人url
- 将env配置文件使用yaml进行管理
"""

import requests

# ip = "127.0.0.1"

# env = {
#     "default": "dev",
#     "host":
#         {
#             "dev": "127.0.0.1",
#             "pre": "127.0.0.2"
#         }
# }
import yaml


class EnvApi:
    """多环境 api"""
    env = yaml.safe_load(open("env.yml"))

    # 二次封装requests，对请求进行定制化
    def send(self, data: dict):
        # data["url"] = str(data["url"]).replace("host", env['pre'])
        data["url"] = str(data["url"]).replace("host", self.env['host'][self.env["default"]])
        res = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return res
