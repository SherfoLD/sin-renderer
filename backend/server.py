import asyncio
import math
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/sin")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    frequency = 200
    interval = 1 / frequency
    x = 0

    try:
        while True:
            y = round(math.sin(2 * math.pi * x), 10)
            await websocket.send_json(
                {"x": x, "y": y}
            )
           
            x += interval
            await asyncio.sleep(interval)

    except Exception as e:
        print(f"Error: {e}")
