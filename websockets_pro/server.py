# Time: 2021/9/3 13:39
# Author: jiangzhw
# FileName: server.py


# 用于构建websocket服务器，在本地8765端口启动，会将接收到的消息加上I got your message:返回回去。
import asyncio
import time

import websockets
# websockets比较适合熟悉Python协程和异步的大佬使用
#
# async def echo(web_socket, path):
#     async for message in web_socket:
#         message = "I got your message: {}".format(message)
#         await web_socket.send(message)
#
#
# asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
# asyncio.get_event_loop().run_forever()


# 主动发消息
async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if str(t).endswith("0"):
                await websocket.send(t)
                break


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
