def add1(x:int,y:int)->int:
    return x+y

a = add1(1,2)
print(a)

# 定义变量指向一个函数，并添加注解
from typing import Callable
f:Callable[[int,int],int] = add1 # [[参数类型],返回值类型]
print(f(100,200))


# 定义函数，产生整数的生成器
from typing import Iterator
def return_num(num:int)->Iterator[int]:
    i = 0
    while i < num:
        yield i
        i += 1

for i in return_num(5):
    print(i)

# 正确：变量b标注为 Iterator[int]（与函数返回值类型一致）
b: Iterator[int] = return_num(5)
for i in b:
    print(i)  # 输出：0,1,2,3,4
