import websockets
import asyncio

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

if __name__ == "__main__":
    PORT = 8765
    HOST = 'localhost'
    start_server = websockets.serve(hello, HOST, PORT)
    print("server is running at {}:{}".format(HOST, PORT))

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()