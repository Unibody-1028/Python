a = 3
print(a)
print(id(a))
print(type(a))


b = '我爱你'
print(b)
print(id(b))
print(type(b))


# 常量
MAX_AGE = 120
print(MAX_AGE)
MAX_AGE = 150
print(MAX_AGE)

# 序列解包赋值实现变量互换
a,b = 1,2
print(a)
print(b)
a,b = b,a
print(a)
print(b)


# 基本数据类型

a = 1
b1 = 3.14
b2 = 314e-2
c = 'abc'
d = True

for i in [a,b1,b2,c,d]:
    print(type(i))
    

import time
