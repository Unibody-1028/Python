import time
def cost_time(func):
    def infunc(*args,**kwargs):
        print("开始计时")
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("耗费时间:",t2-t1)
        return result
    return infunc

class CacheDecorator():
    __cache = {}
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        # 如果缓存中有对应的方法名，则直接返回对应的值
        if self.func.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.func.__name__]
        # 否则就进行计算，并将结果缓存
        else:
            result = self.func(*args,**kwargs)
            CacheDecorator.__cache[self.func.__name__] = result
            return result
@cost_time           #  func1_long_time~~ = cost_time(func1_long_time~)
@CacheDecorator      #  func1_long_time~ = CacheDecorator(func1_long_time)

# func1_long_time = cost_time(CacheDecorator(func1_long_time))

def func1_long_time():
    """模拟耗时较长，每次执行返回结果都一样的情况"""
    print("start func1")
    time.sleep(1)
    print("end func1")
    return 999
if __name__ == '__main__':
    r1 = func1_long_time()
    r2 = func1_long_time()
    print(r1)
    print(r2)
