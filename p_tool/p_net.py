import socket
import struct

def get_ip_from_mac(mac_address):
    # 创建socket对象
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    # 发送ARP请求以获取指定MAC地址的IP地址
    s.bind(('eth0', 0))
    packet = struct.pack("!6s6s2s", '\xff\xff\xff\xff\xff\xff', mac_address.replace(':', '').decode('hex'), '\x08\x06')
    s.send(packet)

    # 接收ARP响应
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth_protocol = struct.unpack("!6s6s2s", raw_data[:14])[2]
        if eth_protocol == '\x08\x06':
            arp_protocol = struct.unpack("!2s2s1s1s2s6s4s6s4s", raw_data[14:42])
            if arp_protocol[4] == '\x00\x02':
                return socket.inet_ntoa(arp_protocol[6])

# 使用示例
mac_address = '48:21:0B:33:11:9F'
ip_address = get_ip_from_mac(mac_address)
print("IP地址:", ip_address)