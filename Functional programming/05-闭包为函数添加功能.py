# 装饰器基础
# 不修改源代码，给代码添加新的功能

def outfunc(func1):

    def infunc(*args,**kwargs):
        print("日志记录,start")
        func1(*args,**kwargs)
        print("日志记录,end")

    return infunc

def func1():
    print("使用功能1")
def func2(a,b,c):
    print("使用功能2",a,b,c)
func1 = outfunc(func1)
func1()
func2 = outfunc(func2)
func2(1,2,3)

