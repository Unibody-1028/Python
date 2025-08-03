from socket import *

s = socket(AF_INET,SOCK_DGRAM)
# 绑定IP和端口
s.bind(("127.0.0.1",8888))
while True:
    print("等待接收数据")
    recv_data = s.recvfrom(1024) # 1024表示本次接收的最大字节数
    recv_content = recv_data[0].decode('utf-8')
    print(f"收到远程信息:{recv_content},来自{recv_data[1]}")
    if recv_content == "88":
        print("结束接收信息")
        break
s.close()

