# 类装饰器

class MylogDecorator():
    def __init__(self,func):
        # 初始化方法：接收被装饰的函数作为参数
        self.func = func
    def __call__(self, *args, **kwargs):
        # 调用方法：当装饰后的函数被调用时，会执行此方法
        print("日志记录...")
        return self.func(*args,**kwargs) # 调用原始函数，并返回其结果
@MylogDecorator
# fun2 = MylogDecorator(fun2)
# 此时fun2已不再是原始函数，而是MylogDecorator类的一个实例。
# 当执行 fun2() 时，由于 fun2 是 MylogDecorator 的实例，
# 且类定义了 __call__ 方法，因此会触发 __call__ 方法的执行
def fun2():
    print("功能2...")

if __name__ == '__main__':
    fun2()