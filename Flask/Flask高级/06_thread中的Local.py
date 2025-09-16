from threading import Thread,local

local = local()
local.request = '这个是请求的数据1'

class MyThread(Thread):
    def run(self):
        local.request = 'final'
        print(f'子线程的内容:{local.request}')

my_thread = MyThread()
my_thread.start()
my_thread.join()

print(f'主线程的内容:{local.request}')