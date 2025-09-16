# @mylog
# @cost_time
# """
# 函数定义阶段:相当于fun2 = cost_time(fun2)
#                 fun2 = mylog(fun2)
#            也相当于:fun2 = mylog(cost_time(fun2))
#
# 执行调用阶段:先执行mylog的内部函数，再执行cost_time的内部函数
# """
# def fun2():
#     pass
# fun2()


import time

def mylog(func):
    print("mylog,start")

    def innerfunc():
        print("日志记录start")
        func()
        print("日志记录end")

    print("mylog,end")

    return innerfunc

def cost_time(func):
    print("cost_time start")
    def innerfunc():
        print("开始计时")
        t1 = time.time()
        func()
        t2 = time.time()
        print("耗费时间:",t2-t1)

    print("cost_time end")
    return innerfunc

@mylog       # fun2~~ = mylog(fun2~)
@cost_time   # fun2~ = cost_time(fun2)
def fun2():
    print("fun2,start")
    time.sleep(3)
    print("fun2,end")
"""
装饰器定义阶段结束后，fun2 = mylog(cost_time(fun2))
执行时，依次执行mylog和cost_time的内部函数(innerfunc,即封装过fun2的函数)
"""


fun2()
# cost_time start
# cost_time end
# mylog,start
# mylog,end
# 日志记录start
# 开始计时
# fun2,start
# fun2,end
# 耗费时间: 3.002222776412964
# 日志记录end