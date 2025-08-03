from socket import *

s = socket(AF_INET,SOCK_DGRAM)
addr = ("127.0.0.1",8888)
while True:
    data = input("请输入信息:")
    s.sendto(data.encode("utf-8"),addr)
    if data == "88":
        print("停止发送数据")
        break

s.close()
