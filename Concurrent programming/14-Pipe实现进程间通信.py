import multiprocessing
from time import sleep

def func1(conn1):
    sub_info = "Hello"
    print(f"进程1---{multiprocessing.current_process().pid}发送数据:{sub_info}")
    conn1.send(sub_info)
    sleep(1)
    print(f"来自进程2:{conn1.recv()}")
def func2(conn2):
    sub_info = "你好"
    print(f"进程2---{multiprocessing.current_process().pid}发送数据:{sub_info}")
    conn2.send(sub_info)
    sleep(1)
    print(f"来自进程1:{conn2.recv()}")
if __name__ == '__main__':
    # 创建管道
    conn1,conn2 = multiprocessing.Pipe()
    # 创建子进程
    process1 = multiprocessing.Process(target=func1,args=(conn1,))
    process2 = multiprocessing.Process(target=func2,args=(conn2,))
    # 启动子进程
    process1.start()
    process2.start()