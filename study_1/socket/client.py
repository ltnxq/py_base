import socket

# 创建套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 5000)
client_socket.connect(server_address)

while True:
    # 输入要发送的消息
    message = input('请输入要发送的消息（输入 quit 结束）：')

    # 发送消息给服务器
    client_socket.send(message.encode())

    if message == 'quit':
        break

    # 接收服务器的回复
    response = client_socket.recv(1024).decode()
    print(f'收到服务器的回复：{response}')

print('连接断开。')

# 关闭套接字
client_socket.close()