# 简单类型变量标注

a:int = 10
b:str = "hello "
c:float = 3.14
d:bool = True
e:bytes = b"Hello world"

# 使用mypy模块可以进行类型检查
# mypy 02-变量类型标注.py

# 复杂类型
from typing import List,Set,Dict,Tuple # python3.10之前需要手动导入
x:List[int] = [1,2,3]
y:Set[str] = {"a","b"}
z:Dict[str,int] = {'a':1,"b":2}
v:Tuple[int] = (1,)
n:Tuple[int,int] = (1,2)
m:Tuple[int,str,bool] = (1,"a",True)
# 定义可变大小的元组，使用省略号
Z:Tuple[int,...] = (1,2,3)



