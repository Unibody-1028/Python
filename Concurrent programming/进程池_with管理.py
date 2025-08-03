import os
from time import sleep
from multiprocessing import Pool

def func1(name):
    print(f"当前进程的ID:{os.getpid()},{name}")
    sleep(2)
    return name

if __name__ == '__main__':
    with Pool(5) as pool:
        args = pool.map(func1,('geek1','geek2','geek3','geek4','geek5','geek6'))
        for a in args:
            print(a)