import os
from multiprocessing import Pool
from time import sleep
def func1(name):
    print(f"当前进程的ID:{os.getpid()},{name}")
    sleep(2)
    return name
def func2(args):
    print(args)


if __name__ == '__main__':
    pool = Pool(5)

    pool.apply_async(func=func1,args=("geek1",),callback=func2)
    pool.apply_async(func=func1,args=("geek2",),callback=func2)
    pool.apply_async(func=func1,args=("geek3",),callback=func2)
    pool.apply_async(func=func1, args=("geek4",))
    pool.apply_async(func=func1, args=("geek5",))
    pool.apply_async(func=func1, args=("geek6",))
    pool.apply_async(func=func1, args=("geek7",))
    pool.apply_async(func=func1, args=("geek8",))

    pool.close()
    pool.join()

