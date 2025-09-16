import os
from time import sleep
from multiprocessing import Pool

def func1(name):
    print(f"当前进程的ID:{os.getpid()},{name}")
    sleep(2)
    return name


if __name__ == '__main__':
    # 创建一个包含5个进程的进程池（with语句会自动管理进程池的生命周期）
    with Pool(5) as pool:
        # 使用map方法将任务分配给进程池
        # 第一个参数是任务函数func1，第二个参数是可迭代的参数列表
        args = pool.map(func1, ('geek1', 'geek2', 'geek3', 'geek4', 'geek5', 'geek6'))

        # 遍历并返回的结果并打印
        for a in args:
            print(a)