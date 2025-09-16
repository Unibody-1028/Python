# 旧版本
from typing import Union

def func_test(num:Union[int,float])->Union[int,float]:
    return num+100
print(func_test(1))
print(func_test(1.1))

# 新版本
def func_test2(num:int|float)->int|float:
    return num+100
print(func_test2(1))
print(func_test2(1.1))