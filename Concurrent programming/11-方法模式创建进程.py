import os
from multiprocessing import Process
from time import sleep


def fun1(name):
    print(f"Process:{name},start")
    print("当前进程ID:",os.getpid())
    print("父进程ID:",os.getppid())

    sleep(3)
    print(f"Process:{name},end")

if __name__ == '__main__':
    print("当前进程ID:",os.getpid())
    # 创建进程
    p1 = Process(target=fun1,args=("p1",))
    p2 = Process(target=fun1, args=("p2",))
    # 启动进程
    p1.start()
    p2.start()

