## 并发编程介绍

### 串行、并行、并发的区别

<img src="assets/image-20250727221733823.png" alt="image-20250727221733823" style="zoom:50%;" />

1. 串行（serial）：一个cpu上，按顺序完成多个任务
2. 并行（parallelism）：指的是任务数小于等于cpu核心数，即任务真的是一起执行
3. 并发（concurrency）：一个cpu采用时间片管理方式，交替的处理多个任务。一般是任务数多于cpu核心数，通过操作系统的各种任务调度算法，实现用多个任务一起执行（实际上总有一些任务在等待分配时间片，因为切换任务的速度很快，看上去是一起执行而已。）

## 进程、线程、协程的区别

![image-20250727222838996](assets/image-20250727222838996.png)

<img src="assets/image-20250728082921435.png" alt="image-20250728082921435" style="zoom:50%;" />



1. 线程是程序执行的最小单位，进程是操作系统分配资源的最小单位
2. 一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线
3. 进程之间相互独立，但同一个进程下的各个线程共享程序的内存空间（包括代码段、数据集、堆等）以及一些进程级的资源（如打开文件和信号），某进程内的线程在其它进程不可见
4. 调度和切换：线程上下文切换比进程上下文切换要快的多

![image-20250728083341800](assets/image-20250728083341800.png)

### 进程是什么？

​	进程（Process）是一个具有一定独立功能的程序关于某个数据集合的一次运行活动

### 线程是什么？

​	线程（Thread）是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。

### 并发编程解决方案

多任务的实现有三种方法

1. 多进程模式
2. 多线程模式
3. 多进程+多线程模式

<img src="assets/image-20250728084005374.png" alt="image-20250728084005374" style="zoom:50%;" />

### 协程是什么？

协程（Coroutines），也叫做纤程（Fiber），是一种在线程中，比线程更加轻量级的存在，由程序员自己写程序管理。

## 同步和异步

同步和异步强调的是消息通信机制（synchronous communication /asynchronous communication ）

​	同步（synchronous communication ）：A调用B，等待B返回结果后，A继续执行。

​	异步（asynchronous communication ）：A调用B，A继续执行，不等待B返回结果；B处理完毕后，通知A，A再做处理。

## 线程（Thread）

1. **线程（Thread）**是操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中的实际运作单位。
2. 线程是程序执行的最小单位，而进程是操作系统分配资源的最小单位。
3. 一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线。
4. 线程拥有自己独立的栈和共享的堆，标准线程由操作系统调度。
5. 线程上下文切换比进程上下文切换要快的多。

### 创建线程

​	Python的标准库提供了两个模块：`_thread`和`threading`,`_thread`是低级模块，`threading`是高级模块，对`_thread`进行了封装。

线程的创建可以通过两种方式：

1. 方法包装
2. 类包装

线程的执行统一通过`start()`方法

### 线程的创建方式（方法包装）

```python
from threading import Thread
from time import sleep

def func1(name):
    print("线程{},start".format(name))
    for i in range(3):
        print("线程:{0},{1}".format(name,i))
        sleep(3)
    print("线程{},end".format(name))


if __name__ == '__main__':
    print("主线程,start")
    # 创建线程
    t1 = Thread(target=func1,args=("t1",))
    t2 = Thread(target=func1,args=("t2",))
    # 启动线程
    t1.start()
    t2.start()

    print("主线程,end")
```

### 线程的创建方式（类包装）

```python
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
```

## join()

​	如果需要等待子线程结束后，再结束主线程，可以使用join()方法

```python
from threading import Thread
from time import sleep

def func1(name):
    print("线程{},start".format(name))
    for i in range(3):
        print("线程:{0},{1}".format(name,i))
        sleep(3)
    print("线程{},end".format(name))
    

if __name__ == '__main__':
    print("主线程,start")
    # 创建线程
    t1 = Thread(target=func1,args=("t1",))
    t2 = Thread(target=func1,args=("t2",))
    # 启动线程
    t1.start()
    t2.start()
    # 主线程会等待t1,t2结束后,再往下执行
    t1.join()
    t2.join()

    print("主线程,end")
```

## 守护线程

​	在行为上还有一种叫守护线程，主要的特征是它的生命周期。主线程死亡，它也就随之死亡。在Python中，线程通过`setDaemon(True|False)`来设置是否为守护线程。

守护线程的作用：

​	守护线程的作用是为其它线程提供便利的服务，守护线程最典型的应用就是GC（垃圾收集器）。

```python
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
```

## 全局锁GIL问题

### Python GIL(Global Interpreter Lock)

​	Python代码的执行由Python虚拟机(也叫解释器主循环,CPython版本)来控制，Python在任意时刻只有一个线程在解释器中运行，对虚拟机的访问由全局解释器锁（GIL）控制。

![image-20250728175339584](assets/image-20250728175339584.png)

## 线程同步和互斥锁

### 线程同步

​	**处理多线程问题时，多个线程访问同一个对象，并且某些线程还想修改这个对象。这时候，我们就需要用到“线程同步”。线程同步其实就是一种等待机制，多个需要同时访问此对象的线程进入这个对象的等待池形成队列，等待前面的线程使用完成后，下一个线程再使用。**

### 锁机制实现线程同步

锁机制注意事项：

1. 必须使用同一个锁对象
2. 互斥锁的作用就是保证同一时刻只能有一个线程去操作共享的数据，保证共享的数据不会出现错误
3. 使用互斥锁能确保**某段关键代码可以由一个线程从头到尾完整执行**	
4. 使用互斥锁会影响代码的执行效率
5. 同时拥有多把锁，容易出现死锁

### 互斥锁

​	互斥锁：对共享数据进行锁定，保证同一时刻只能有一个线程去操作。

**互斥锁是多个线程一起抢夺，得到锁的线程先执行，没有抢到锁的进程需要等待，互斥锁使用完毕释放后，其它的线程再去抢这个锁**

```
# 互斥锁
from threading import Thread,Lock
from time import sleep


class Account:
    def __init__(self,name,money):
        self.name = name
        self.money = money

# 模拟提款操作
class Drawing(Thread):
    def __init__(self,drawingNum,account):
        # 调用父类初始化函数
        super().__init__()
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0
    def run(self):
        global lock
        # 获取锁
        #lock.acquire()
        with lock:
            if self.account.money<self.drawingNum:
                print("账户余额不足")
                return
            #sleep(1) # 测试冲突问题
            self.account.money -= self.drawingNum
            self.expenseTotal += self.drawingNum

            print("账户名:{},余额:{}".format(self.account.name,self.account.money))
            print("账户名:{},总共取出金额为:{}".format(self.account.name,self.expenseTotal))
        #lock.release()
if __name__ == '__main__':
    a1 = Account("Jack",100)
    # 互斥锁
    lock = Lock()
    draw1 = Drawing(80,a1) # 第一个取钱的线程
    draw2 = Drawing(100,a1)
    # 启动线程
    draw1.start()
    draw2.start()

```

### 死锁

在多线程程序中，死锁问题很大一部分是由一个线程同时获取多个锁造成的

## 信号量(Semaphore)

​	信号量控制同时访问资源的数量。信号量和锁类似，锁同一时间只允许一个对象（进程）通过，信号量同一时间允许多个对象（进程）通过。

**应用场景**

1. 在读写文件时，一般只能有一个线程在写，而读可以有多个线程同时进行，如果需要限制同时读文件的线程个数，就可以使用信号量。（如果使用互斥锁，就是限制同一时刻只能有一个线程读取文件）
2. 爬虫抓取数据

**原理**

​	信号量底层实现就是一个内置的计数器。每当资源获取时（调用acquire）计数器-1，资源释放时（调用release）计数器+1。

## 事件(Event)

事件Event主要用于唤醒正在阻塞的进程。

**原理**

​	Event对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初始情况下，event对象中的信号标志被设置为假。**如果有线程等待一个event对象，而这个event对象的标志为假，那么这个线程将会被一直阻塞直到该标志为真。**一个线程如果将一个event对象的信号标志设置为真，那么它将唤醒所有等待这个event对象的线程。<u>如果一个线程等待一个已经被设置为真的event对象，那么它将忽略这个事件，继续执行。</u>

![image-20250728220541207](assets/image-20250728220541207.png)

```
import threading
import time


def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print(name+"已经启动")
    print(name+"已经进入就餐状态")
    time.sleep(1)
    event.wait()
    # 收到事件通知后进入运行状态
    print(name+"收到通知")
    print("开始干饭")

if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=chihuoguo,args=("Tom",))
    t2 = threading.Thread(target=chihuoguo,args=("Jack",))
    # 开启线程
    t1.start()
    t2.start()

    time.sleep(5)
    # 发送事件通知
    print("主线程通知：开始干饭")
    event.set()
```

## 生产者消费者模式

### 缓冲区

缓冲区是实现并发的核心，缓冲区的设置有3个好处。

1. 实现线程的并发协作

    ​	有缓冲区以后，生产者线程只需要往缓冲区里面放置数据，而不需要管理消费者消费；同样，消费者只需要从缓冲区拿数据即可。这样就实现了"生产者线程"和"消费者线程"的分离

2. 解耦了生产者和消费者

    生产者不需要和消费者交互

3. 解决忙闲不均，提高效率

    生产者/消费者进程受阻时，消费者/生产者仍然可以从缓冲区内拿取/存放数据。

### 缓冲区和queue对象

​	从一个线程向另一个线程发送数据最安全的方式是使用queue库里的队列。创建一个被多个线程共享的Queue对象，这些线程通过使用put()和get()操作向队列里添加或删除元素。Queue对象已经包含了必要的锁，所以可以通过它在多个线程间安全的共享数据。

```
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
```

## 进程Process

​	![image-20250729153006543](assets/image-20250729153006543.png)

​	进程(Process)：拥有自己独立的堆和栈，既不共享堆，也不共享栈，进程由操作系统调度；进程切换时耗费的资源很多，效率低。

### 进程的优缺点

进程的优点：

1. 可以使用计算机多核，进行任务的并行执行，提高执行效率
2. 运行不受其它进程影响，创建方便
3. 空间独立，数据安全

进程的缺点：

-  进程的创建和销毁消耗的系统资源较多

### 进程的创建方式

Python的标准库提供了：`multiprocessing`

进程的创建可以通过两种方式：

1. 方法包装
2. 类包装

创建进程后，使用start()启动进程。

####  方法模式创建进程

```python
import os
from multiprocessing import Process
from time import sleep


def fun1(name):
    print(f"Process:{name},start")
    print("当前进程ID:",os.getpid())
    print("父进程ID:",os.getppid())

    sleep(3)
    print(f"Process:{name},end")

if __name__ == '__main__':
    print("当前进程ID:",os.getpid())
    # 创建进程
    p1 = Process(target=fun1,args=("p1",))
    p2 = Process(target=fun1, args=("p2",))
    # 启动进程
    p1.start()
    p2.start()
```

#### 类模式创建进程

```python
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
```

## Queue实现进程通信

```python
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
```

## Pipe实现进程间通信

![image-20250802004559597](assets/image-20250802004559597.png)

```
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
```

## Manager管理器

​	Manager管理器实现进程间通信

```python
from multiprocessing import Manager,Process

def func(name,m_list,m_dict):
    m_list.append("你好")
    m_dict["name"] = "Jack"


if __name__ == '__main__':
    with Manager() as mgr:
        m_list = mgr.list()
        m_dict = mgr.dict()
        m_list.append("Hello")

        # 两个进程间不能直接互相使用对象，需要互相传递
        p1 = Process(target=func,args=("p1",m_list,m_dict))
        p1.start()
        p1.join()
        print(f"主进程{m_dict}")
        print(f"主进程{m_list}")

```

## 进程池(Pool)

​	Python提供了更好的管理多个进程的方式，即进程池。进程池可以提供指定数量的进程给用户使用，当有新的请求提交到进程池中时，如果进程池未满，则会创建一个新的进程用来执行该请求；反之，如果池中的进程书已经达到规定的最大值，那么请求就会等待，只要进程池中有进程空闲下来，请求就会得到相应。

​    使用进程池的优点：

1. 提高效率，节省开辟进程和开辟内存空间的时间及销毁进程的时间。
2. 节省内存空间

![image-20250802011512622](assets/image-20250802011512622.png)

```
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


```

## 协程Coroutines

​	协程，Coroutines，也叫做纤程(Fiber)，全程是协同程序，用来实现任务协作，是一种在线程中更加轻量级的存在，由程序员自己写程序来管理。

​	当出现IO阻塞时，CPU一直等待IO返回，处于空闲状态，此时可以使用协程来执行其它任务，当IO返回结果后，再回来处理数据。充分利用了IO等待的时间，提高了效率。

### 协程的核心(控制流的让出和恢复)

1. 每个协程都有自己的执行栈，可以保存自己的执行现场
2. 可以由用户程序按需创建协程(比如：遇到IO操作)
3. 协程**"主动让出(yield)"执行权**时，会保存执行现场(保存中断时的寄存器上下文和栈)，然后切换到其它协程
4. 协程**恢复执行(resume)**时，根据之前保存的执行现场恢复到中断前的状态，继续执行，这样就通过协程实现了轻量级的由用户态调度的多任务模型。

### 协程和多线程的比较

![image-20250802014258417](assets/image-20250802014258417.png)

![image-20250802014319763](assets/image-20250802014319763.png)

### 协程的优点

1. 由于自身带有上下文和栈，无需线程上下文切换的开销，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
2. 无需原子操作的锁定及同步的开销
3. 方便切换控制流，简化编程模型
4. 单线程内就可以实现并发的效果，最大限度地利用CPU，且可扩展性高，成本低，适用于高并发处理

### 协程的缺点

1. 无法利用多核资源：协程的本质是个单线程，它不能同时将多核心处理器充分利用，协程需要与进程配合才能运行在多核心上。
2. CPU密集型应用才有使用协程的必要

## 使用yield实现协程(已淘汰)

​	协程发展阶段：

1. 最初的生成器变形`yield/send`
2. 引入`@asyncio.coroutine`和`yield from`
3. Python3.5版本后，引入`async/await`关键字

```
import time

def func1():
    for i in range(3):
        print(f"北京第{i}次打印")
        yield # 只要方法包含了yield，就会变成一个生成器
        time.sleep(1)

def func2():
    g = func1()
    print(type(g))
    for k in range(3):
        print(f"上海第{k}次打印")
        next(g) # 继续执行func1的代码
        time.sleep(1)

if __name__ == '__main__':
    # 有了yield，实现了两个任务的切换+保存状态
    t1 = time.time()
    func2()
    t2 = time.time()
    print(f"耗时:{t2-t1}")
```

## asyncio实现协程

1. 正常的函数执行时是不会中断的，需要函数中断，就需要加`async`
2. `async`用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，再去执行其它异步函数，等到挂起条件消失后，再回来执行原函数。
3. `await`用来声明程序挂起，如果异步程序执行到某一步时需要等待的时间很长，就将程序挂起，去执行其它的异步程序
4. `asyncio`是Python3.5之后的协程模块，是Python实现并发重要的包，这个包使用时间循环驱动实现并发

```
import asyncio
import time

async def func1(): # asyncio表示方法是异步的
    for i in range(3):
        print(f"北京:第{i}次打印")
        await asyncio.sleep(1)
    return "func1执行完毕"

async def func2(): # asyncio表示方法是异步的
    for k in range(3):
        print(f"上海:第{k}次打印")
        await asyncio.sleep(1)
    return "func2执行完毕"

async def main():
    res = await asyncio.gather(func1(),func2())
    # await 异步执行func1方法
    # 返回值为函数的返回值列表
    print(res)
if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(f"耗时:{t2-t1}")
```







​	























