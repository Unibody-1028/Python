# 第一个装饰器
def writelog():
    print("日志记录")

def outer_func(function):
    def inner_func(*args,**kwargs):
        function(*args,**kwargs)
        writelog()
    return inner_func

@outer_func  # 等价于 func1 = outer_func(func1)
def func1():
    print("使用功能1")

@outer_func  # 等价于 func2 = outer_func(func2)
def func2(a,b):
    print("使用功能2",a,b)

#func1 = outer_func(func1)
#func2 = outer_func(func2)
func1()
func2(100,200)



"""
def print_log():
    print("记录日志")
def mylog(function):
    def inner(*args,**kwargs):
        function(*args,**kwargs)
        print_log()
    return inner
@mylog
def func1():
    print("功能1:")
@mylog
def func2(a,b):
    print("功能2:",a,b)
func1()
func2(1,2)
"""
