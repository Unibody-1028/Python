import threading
import time


def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print(name+"已经启动")
    print(name+"已经进入就餐状态")
    time.sleep(1)
    event.wait()
    # 收到事件通知后进入运行状态
    print(name+"收到通知")
    print("开始干饭")

if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=chihuoguo,args=("Tom",))
    t2 = threading.Thread(target=chihuoguo,args=("Jack",))
    # 开启线程
    t1.start()
    t2.start()

    time.sleep(5)
    # 发送事件通知
    print("主线程通知：开始干饭")
    event.set()