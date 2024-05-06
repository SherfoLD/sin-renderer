import asyncio
import math
from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

@app.websocket("/sin")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    frequency = 4
    interval = 1 / frequency
    x = 0

    try:
        while True:
            y = round(math.sin(2 * math.pi * x), 10)
            await websocket.send_text(f"{x},{y}")

            x += interval
            await asyncio.sleep(interval)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
