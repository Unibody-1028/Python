from threading import Thread
from time import sleep

def func1(name):
    print("线程{},start".format(name))
    for i in range(3):
        print("线程:{0},{1}".format(name,i))
        sleep(3)
    print("线程{},end".format(name))


if __name__ == '__main__':
    print("主线程,start")
    # 创建线程
    t1 = Thread(target=func1,args=("t1",))
    t2 = Thread(target=func1,args=("t2",))
    # 启动线程
    t1.start()
    t2.start()

    print("主线程,end")