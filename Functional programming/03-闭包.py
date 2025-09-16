def outer():
    a = 1
    def inner():
        nonlocal a # 在内层函数中，声明外层使用的局部变量
        print("a:",a)
        a += 1

    return inner
inn = outer()
inn()
inn()

# a: 1
# a: 2



