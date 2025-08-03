from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    # 重写run函数
    def run(self):
        name = self.name
        print("线程:{},start".format(name))
        for i in range(3):
            print("线程:{0},{1}".format(name, i))
            sleep(3)
        print("线程:{},end".format(name))

if __name__ == '__main__':
    print("主线程,start")
    # 创建线程
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    # 手动启动线程 后自动调用run()函数
    t1.start()
    t2.start()

    print("主线程,end")