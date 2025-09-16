import time
import gc
class AA():
    def __new__(cls, *args, **kwargs):
        print("new")
        return super(AA,cls).__new__(cls)
    def __init__(self):
        print(f"object born at {hex(id(self))}")
    def __del__(self):
        print(f"{hex(id(self))} 被系统回收")
def start():
    while True:
        a = AA()
        b = AA()
        a.v = b
        b.v = a
        del a
        del b
        print(gc.get_threshold())
        print(gc.get_count())
        time.sleep(0.2)
# 手动关闭垃圾回收机制
#gc.disable()
start()