import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    print("Nuevo cliente conectado")
    clients.add(websocket)
    try:
        async for message in websocket:
            # retransmite audio a todos los clientes excepto al que lo envió
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except:
        pass
    finally:
        print("Cliente desconectado")
        clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
