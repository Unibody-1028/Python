import asyncio
import time

async def func1(): # asyncio表示方法是异步的
    for i in range(3):
        print(f"北京:第{i}次打印")
        await asyncio.sleep(1)
    return "func1执行完毕"

async def func2(): # asyncio表示方法是异步的
    for k in range(3):
        print(f"上海:第{k}次打印")
        await asyncio.sleep(1)
    return "func2执行完毕"

async def main():
    res = await asyncio.gather(func1(),func2())
    # await 异步执行func1方法
    # 返回值为函数的返回值列表
    print(res)
if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(f"耗时:{t2-t1}")