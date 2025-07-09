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


import time 
time1 = time.time()
a = ''
for i in range(1000000):
    a += 'stx'
time2 = time.time()

li = []
for i in range(1000000):
    li.append('stx')
time3 = time.time()
b = ''.join(li)
time4 = time.time()

print('+操作耗费时间：'+str(time2-time1))
print('join操作耗费时间：'+str(time4-time3))


# 字符串格式化
a = '姓名:{0},年龄:{1}'
b = a.format('joe','22')
print(b)

c = '姓名:{name},年龄:{age}'
d = c.format(name='Jack',age='11')
print(d)

# 数字格式化
a = '{:.2f}'
print(a.format(3.1415))



import io 
s = 'abcdefg' # s仍然不可变
sio = io.StringIO(s) # sio就是可变字符串
print(sio)
print(sio.getvalue())
sio.seek(3) #指针到索引3这个位置
sio.write("@@")
print(sio.getvalue())


import random
a = [10,20,30,40]
random.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)



a = (i for i in range(10))
b = tuple(a)
print(b)

c = (i for i in range(3))
print(c.__next__())
print(c.__next__())
print(c.__next__())

# 字典
a = {'name':'Jack','age':18}
b = dict(name='Jack',age=18)
c = dict([('name','Jack'),('age',18)])
d = {}
e = dict()

print(a)
print(b)
print(c)
print(d)
print(e)

k = ['name','age','job']
v = ['Jack',18,'programmer']
d = dict(zip(k,v))
print(d)

f = dict.fromkeys(['name','age','job'])

print(f)

print(d.get('name'))
print(d.get('age1',0))


a = {10,20,30}
b = {100,20,300}

c = a|b
print(c)
c = a&b
print(c)
c = a-b
print(c)