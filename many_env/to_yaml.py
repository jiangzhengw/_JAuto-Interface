# Time: 2021/4/27 16:55
# Author: jiangzhw
# FileName: to_yaml.py
import yaml


def to_taml(file, data):
    # 打开一个文件（如果没有则创建），将数据存成yaml的形式
    with open(file, "w") as f:
        yaml.safe_dump(data, stream=f)


if __name__ == "__main__":
    env = {
        "default": "dev",
        "host":
            {
                "dev": "127.0.0.1",
                "pre": "127.0.0.2",
                "prd": "127.0.0.3"
            }
    }
    to_taml("env.yml", env)
