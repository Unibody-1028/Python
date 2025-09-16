# send的作用是唤醒并继续执行，发送一个信息到生成器内部
def foo():
    print("start")
    i = 0
    while i<3:
        temp = yield i
        print(f"temp:{temp}")
        i = i+1
    print("end")
g = foo()
print(next(g)) # g.__next__()
print("*" * 20)
print(g.send(1))
print(next(g))