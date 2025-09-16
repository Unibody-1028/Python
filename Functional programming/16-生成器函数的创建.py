'''
1.函数有了yield之后，调用它就会生成一个生成器
2.yield作用：程序挂起，返回相应的值，下次从下一个语句开始执行。
3.return 在生成器中代表生成器终止，直接报错：StopIteration
4.next方法作用：唤醒并继续执行
'''
def test():
    print("start")
    i = 0
    while i<3:
        print(f"i:{i}")
        yield i
        #print(f"i:{i}")
        i += 1
    print("end")
    return "done"

if __name__ == '__main__':
    a = test()
    print(a)
    a.__next__()
    a.__next__()
    a.__next__()
    a.__next__()

