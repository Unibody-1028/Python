# 信号量测试
from threading import Semaphore, Thread
from time import sleep

# 一个房间，一次只允许两个人进入
def house(name,se):
    with se:
        print(f"{name}进入房间")
        sleep(2)
        print(f"{name}走出房间")

if __name__ == '__main__':

    se = Semaphore(2) # 信号量对象
    for i in range(5):
        t = Thread(target=house,args=(f"thread{i}",se))
        t.start()