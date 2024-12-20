
import os
from dotenv import load_dotenv
import asyncio
import bleak
import numpy as np
from bleak import BleakClient
load_dotenv()
audio_frames = []

device_id = "BC1026C2-68D5-1B67-EDED-527CF1783A25" #Please enter the id of your device (that is, the device id used to connect to your BT device here)
# device_id = "FD0EDA25-0E3D-3F50-78F5-D6A73643EEA1"
battery_uuid = "0000180f-0000-1000-8000-00805f9b34fb" #dont change this
battery_read_uuid = "00002a19-0000-1000-8000-00805f9b34fb"
read_or_clear = 0 # 0 for read, 1 for clear
file_num = 1
count = 1
async def main():
        
        global device_uuid
        global storage_uuid
        global count

        async with BleakClient(device_id) as client:

                async def on_notify(sender: bleak.BleakGATTCharacteristic, data: bytearray):
                        print(ord(data))
                stuff = await client.start_notify(battery_read_uuid, on_notify)
                await asyncio.sleep(1)   
                while True:
                    await asyncio.sleep(1)

        
if __name__ == "__main__":
    asyncio.run(main())
