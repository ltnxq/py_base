import asyncio
from bleak import BleakScanner ,BleakClient

async def scan():
    devices = await BleakScanner.discover(timeout=15)
    for dev in devices:
        print("发现设备名称:{},mac地址:{}".format(dev.name,dev.address))

        async with BleakClient(dev) as client:
            services = await client.get_services()
            for service in services:
                print("服务 UUID:{}".format(service.uuid))

async def connect_and_write(address):
    async with BleakClient(address) as client:
        print("成功连接蓝牙设备")
        services = client.get_services()
        for service in services:
            print("服务uuid:{}",service.uuid)
            for character in service.characteristics:
                print(character)
                print("特征值uuid:{}".format(character.uuid))
                print("特征值属性:{}".format(character.properties))
    print("断开连接")

loop = asyncio.get_event_loop()
#loop.run_until_complete(scan())


device_address = "4c:ea:ae:e5:46:c4"
#loop.run_until_complete(connect_and_write(device_address))
async def find_device():
  device = await BleakScanner.find_device_by_address(device_address, timeout=20.0)
  if not device:
      print("not find device by address")
  else:
      print(device)

#loop.run_until_complete(find_device())
loop.run_until_complete(connect_and_write(device_address))
