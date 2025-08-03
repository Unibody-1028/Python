from multiprocessing import Process, Manager
from time import sleep


class MyProcess(Process):
    def __init__(self, name, mq):
        super().__init__()
        self.name = name
        self.mq = mq

    def run(self):
        print(f"Process:{self.name}, 启动")

        # 从队列获取数据
        data = self.mq.get()
        print(f"Process:{self.name}, get Data:{data}")
        sleep(1)

        print(f"Process:{self.name}, 终止")


if __name__ == '__main__':
    # 使用Manager创建队列，解决macOS上的兼容性问题
    manager = Manager()
    mq = manager.Queue(maxsize=3)

    mq.put("1")
    mq.put("2")
    mq.put("3")

    # 进程列表
    p_list = []
    for i in range(3):
        p = MyProcess(f"p{i + 1}", mq)
        p_list.append(p)

    # 启动所有进程
    for p in p_list:
        p.start()

    # 等待所有进程完成
    for p in p_list:
        p.join()
