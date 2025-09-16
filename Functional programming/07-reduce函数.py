from functools import reduce
import time

# reduce实现累加
def add(x,y):
    return x+y
sum = reduce(add,[1,2,3,4,5])
print(sum)

#---------------------------------------

t1 = time.time()
# reduce实现阶乘


sum = reduce(lambda x,y:x*y,range(1,101))
print(sum)
t2 = time.time()
print(f"reduce阶乘花费时间:",t2-t1)
#reduce阶乘花费时间: 1.2159347534179688e-05
#---------------------------------------

t3 = time.time()
def func1(x):
    if x == 0:
        return 1
    else:
        return x*func1(x-1)
sum = func1(100)
print(sum)
t4 = time.time()

print(f"普通阶乘花费时间:",t4-t3)
#普通阶乘花费时间: 1.7881393432617188e-05