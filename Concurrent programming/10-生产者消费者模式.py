from queue import Queue
from threading import Thread
from time import sleep


def producer():
    while True:
        global num
        num += 1
        if queue.qsize() < 8:
            print("正在生产{}号馒头".format(num))
            queue.put("馒头{}号".format(num))
        else:
            print("馒头框已满，等待消费中")
        sleep(1)

def consumer():
    while True:
        print("消费{}".format(queue.get()))
        sleep(1)

if __name__ == '__main__':
    num = 0
    queue = Queue()
    # 创建生产者消费者线程
    p1 = Thread(target=producer)
    c1 = Thread(target=consumer)
    # 指定为守护线程
    p1.daemon = True
    c1.daemon = True
    # 启动线程
    p1.start()
    c1.start()
    #
    sleep(10)
    print("主线程结束，守护线程将随之终止，不再生产消费馒头")






