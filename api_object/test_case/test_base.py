# Time: 2021/4/30 12:01
# Author: jiangzhw
# FileName: test_base.py
from api_object.api.api import API


class TestBase:
    """test base"""

    def setup(self):
        self.api = API()
