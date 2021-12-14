# Time: 2021/9/3 13:42
# Author: jiangzhw
# FileName: client.py


# 模拟服务端：和指定url建立websocket连接，并发送消息，然后等待接收消息，并将消息打印出来。

import asyncio

import websockets


# async def hello(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Hello world!")
#         recv_text = await websocket.recv()
#         print(recv_text)
#
#
# asyncio.get_event_loop().run_until_complete(
#     hello('ws://localhost:8765'))


# 主动发送消息

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print("< Hello world!")
        while True:
            recv_text = await websocket.recv()
            print("> {}".format(recv_text))


asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8765'))
