from socket import *
from threading import Thread


def recv_data():
    while True:
        recv_data = client_socket.recv(1024)
        print(f"服务器说:{recv_data.decode('utf-8')}")
        if recv_data.decode('utf-8') == "88":
            break

def send_data():
    while True:
        msg = input("请输入信息:")
        client_socket.send(msg.encode("utf-8"))
        if msg == "88":
            break



if __name__ == '__main__':
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect(("127.0.0.1",50000))


    t1 = Thread(target=send_data)
    t2 = Thread(target=recv_data)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    client_socket.close()