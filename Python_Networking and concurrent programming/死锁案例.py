from threading import Lock, Thread
from time import sleep


def func1():
    lock1.acquire()
    print("t1获得lock1")
    # 模拟死锁的情况
    sleep(2)

    lock2.acquire()
    print("t1获得lock2")

    lock1.release()
    print("t1释放lock1")
    lock2.release()
    print("t1释放lock2")

def func2():

    lock2.acquire()
    print("t2获得lock2")
    lock1.acquire()
    print("t2获得lock1")

    lock1.release()
    print("t2释放lock1")
    lock2.release()
    print("t2释放lock2")


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
