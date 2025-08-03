from socket import *

server_socket = socket(AF_INET,SOCK_STREAM) # 建立TCP套接字
server_socket.bind(("127.0.0.1",8888))
server_socket.listen(5) # 设置最大监听数
print("等待接收连接请求")
client_socket,client_info = server_socket.accept() # 一直阻塞直到客户连接到达
recv_data = client_socket.recv(1024) # 指定本次接收的最大字节数
print(f"收到信息:{recv_data.decode('utf-8')},来自{client_info}")


client_socket.close()
server_socket.close()


