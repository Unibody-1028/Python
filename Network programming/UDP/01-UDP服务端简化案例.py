from socket import *

s = socket(AF_INET,SOCK_DGRAM) # 创建UDP类型的套接字
s.bind(("127.0.0.1",8888)) # 绑定端口，IP不写则绑定到所有网络接口8888端口
# 如果想限制为「仅本地可访问」，则需要明确写 '127.0.0.1'；
# 如果想允许所有网络接口访问，用 '' 或 '0.0.0.0' 即可（无需写具体 IP）
print("等待接收数据！")
recv_data = s.recvfrom(1024) # 1024表示本次接收的最大字节数
print(f"收到远程信息:{recv_data[0].decode('utf-8')},来自{recv_data[1]}")

s.close()


