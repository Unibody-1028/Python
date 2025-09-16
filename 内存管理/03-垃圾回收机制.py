import sys
class AA:
    def __new__(cls, *args, **kwargs):
        print("创建内存空间")
        return super(AA,cls).__new__(cls)

    def __init__(self):
        print(f"{hex(id(self))}")
    def __del__(self):
        print("bye")
a = AA()
print(f"a的引用计数为:{sys.getrefcount(a)}")
b = a
print(f"a的引用计数为:{sys.getrefcount(a)}")
b = 100
print(f"a的引用计数为:{sys.getrefcount(a)}")
print("程序结束")

import gc
# 返回当前状态链上的对象数量
a = gc.get_count()
print(a)
# 返回阈值
a = gc.get_threshold()
print(a)



