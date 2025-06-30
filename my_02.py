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
del MAX_AGE
# 序列解包赋值实现变量互换
a,b = 1,2
print(a)
print(b)
a,b = b,a
print(a)
print(b)
del a,b

# 基本数据类型

a = 1
b1 = 3.14
b2 = 314e-2
c = 'abc'
d = True

for i in [a,b1,b2,c,d]:
    print(type(i))
    del i
    

import time
# 以秒为单位
b = time.time()
print(b)
del b

# 文件模式下缓存数字
a = 257
b = 257
print(id(a))
print(id(b))
print(a is b)
del a,b

s = '''
a
a. a
a
'''
print(s)

#换行
a = 'I\nlove\nyou'
#制表符
b = 'ni\thao'
#转义字符
c = 'I\'m Tom'
print(a)
print(b)
print(c)
del a,b,c


a = 'abcd'
# 将字符b换成字符a
b = a.replace('b','a')
print(a)
print(b)
print(b is a)

# 字符串分割、合并
a = 'I love You'
b = a.split('o')
print(b)
c = ['aa','bb','cc']
b = ''.join(c)
print(b)
e = '*'.join(c)
print(e)

