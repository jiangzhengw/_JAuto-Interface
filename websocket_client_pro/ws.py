# Time: 2021/9/3 14:38
# Author: jiangzhw
# FileName: ws.py
import websocket

# 1、建立连接
ws = websocket.create_connection("ws://127.0.0.1:5000")
# 2、获取连接状态
print("获取连接状态：", ws.getstatus())
# 3、发送请求参数
ws.send('发送数据 hello jzw')
# 4、获取返回结果
result = ws.recv()
print("接收结果：", result)
# 5、关闭连
ws.close()
