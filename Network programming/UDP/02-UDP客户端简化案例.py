from socket import *

s = socket(AF_INET,SOCK_DGRAM) # 创建UDP类型的套接字
addr = ("127.0.0.1",8888)

data = input("请输入: ")
# 发送数据
s.sendto(data.encode('utf-8'),addr)
s.close()