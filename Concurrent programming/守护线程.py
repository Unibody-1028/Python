from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,name):
        # 自动查找并调用父类Thread的初始化方法
        super().__init__()
        self.name = name
    def run(self):
        for i in range(3):
            print("thread:{0},{1}".format(self.name,i))
            sleep(3)


if __name__ == '__main__':
    print("主线程,start")
    # 类方式创建线程
    t1 = MyThread("t1")
    # 将t1设置为守护线程
    t1.daemon = True
    #t1.setDaemon(True)
    # 启动线程
    t1.start()
    print("主线程,end")
