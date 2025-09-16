import time


def func1():
    for i in range(3):
        print(f"北京:第{i}次打印")
        time.sleep(1)
    return "func1执行完毕"


def func2():
    for j in range(3):
        print(f"上海:第{j}次打印")
        time.sleep(1)
    return "func2执行完毕"


def main():
    func1()
    func2()
if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print(f"耗时:{t2-t1}")




