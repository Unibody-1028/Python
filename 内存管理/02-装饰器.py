'''
类装饰器:
    在不修改源代码的前提下，增加新的功能
'''
class AAA():
    def __init__(self,func):
        print("我是AAA.__init__()")
        self.func = func
    def __call__(self, *args, **kwargs):
        print("调用传入的函数")
        self.func(*args,**kwargs)

@AAA     # test1 = AAA(test1)
def test1():
    print("功能1")

test1()