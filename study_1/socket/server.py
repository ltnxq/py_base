import socket

# 创建套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口号
server_address = ('localhost', 5000)
server_socket.bind(server_address)

# 监听来自客户端的连接请求
server_socket.listen(1)

print('服务器启动，等待客户端连接...')

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print(f'客户端 {client_address} 已连接。')

while True:
    # 接收客户端发送的消息
    data = client_socket.recv(1024).decode()

    if data == 'quit':
        break

    print(f'收到来自客户端的消息：{data}')

    # 发送回复给客户端
    response = f'已收到消息：{data}'
    client_socket.send(response.encode())

print('客户端断开连接。')

# 关闭套接字
client_socket.close()
server_socket.close()