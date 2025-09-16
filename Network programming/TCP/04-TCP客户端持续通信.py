from socket import *
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(("127.0.0.1",8888)) # 连接服务端
while True:
    msg = input("请输入内容:")
    client_socket.send(msg.encode("utf-8"))
    if msg == "88":
        break
    # 接收服务器端数据
    recv_data = client_socket.recv(1024)
    print(f"收到:{recv_data.decode('utf-8')}")

client_socket.close()