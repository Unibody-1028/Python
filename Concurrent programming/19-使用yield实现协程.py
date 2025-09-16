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


