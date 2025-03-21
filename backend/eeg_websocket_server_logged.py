
import asyncio
import websockets
import json
import csv
import time
from collections import deque
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer

buffer_size = 10
eeg_buffer = {
    "alpha": [deque(maxlen=buffer_size) for _ in range(4)],
    "beta": [deque(maxlen=buffer_size) for _ in range(4)],
    "theta": [deque(maxlen=buffer_size) for _ in range(4)],
}

latest_eeg_data = {
    "alpha": [0, 0, 0, 0],
    "beta": [0, 0, 0, 0],
    "theta": [0, 0, 0, 0]
}

csv_file = open("eeg_log.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["timestamp", "band", "ch1", "ch2", "ch3", "ch4"])

def eeg_handler(unused_addr, *args):
    band = unused_addr.split("/")[-1]
    if band in eeg_buffer:
        for i in range(4):
            eeg_buffer[band][i].append(args[i])
        latest_eeg_data[band] = [
            round(sum(eeg_buffer[band][i]) / len(eeg_buffer[band][i]), 6)
            for i in range(4)
        ]
        timestamp = time.time()
        csv_writer.writerow([timestamp, band] + latest_eeg_data[band])
        csv_file.flush()

async def start_osc_server(ip="0.0.0.0", port=5000):
    dispatcher = Dispatcher()
    dispatcher.map("/muse/elements/alpha_absolute", eeg_handler)
    dispatcher.map("/muse/elements/beta_absolute", eeg_handler)
    dispatcher.map("/muse/elements/theta_absolute", eeg_handler)

    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()
    return transport, protocol

async def websocket_handler(websocket, path):
    while True:
        await websocket.send(json.dumps(latest_eeg_data))
        await asyncio.sleep(0.1)

async def main():
    osc_transport, osc_protocol = await start_osc_server()
    ws_server = await websockets.serve(websocket_handler, "0.0.0.0", 8765)
    print("EEG WebSocket server running on ws://0.0.0.0:8765")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
