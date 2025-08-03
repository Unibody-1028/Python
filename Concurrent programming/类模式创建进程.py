from multiprocessing import Process
from time import sleep
from tkinter.font import names


class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Process:{self.name},start")
        sleep(3)
        print(f"Process:{self.name},end")
if __name__ == '__main__':
    # 创建进程
    p1 = MyProcess("p1")
    p2 = MyProcess("p2")

    # 启动进程
    p1.start()
    p2.start()
