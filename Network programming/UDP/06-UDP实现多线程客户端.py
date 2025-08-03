from socket import *
from threading import Thread


def recv_data():
    while True:
        recv_data = s.recvfrom(1024)  # 指定本次接收的最大字节数
        recv_content = recv_data[0].decode("utf-8")
        print(f"收到远程信息:{recv_content},来自{recv_data[1]}")
        if recv_content == "88":
            print("结束聊天")
            break


def send_data():
    addr = ("127.0.0.1", 8888)
    while True:
        data = input("请输入:")
        s.sendto(data.encode("utf-8"), addr)
        if data == "88":
            print("结束聊天")
            break


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(("127.0.0.1", 8889))
    # 创建两个线程
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    s.close()