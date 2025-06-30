# Python

## 对象

​	Python中一切都是对象。
​	每个对象由：标识（identity）、类型（type）、值（value）组成。

![image-20250629233917045](/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250629233917045.png)

​	对象的本质就是：一个内存块，拥有特定的值，支持特定类型的相关操作。

## 引用

​	在Python中，变量也称为对象的引用（reference）。变量存储的就是对象的地址。变量通过地址引用（指向）了对象。
​	变量位于：栈内存。
​	对象位于：堆内存。
​	Python是动态类型的语言：变量不需要显示声明类型。根据变量引用的对象，Python解释器自动确定数据类型。

## 标识符

![image-20250629235554806](/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250629235554806.png)

![image-20250629235907769](/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250629235907769.png)

## 删除变量和垃圾回收机制

​	可以通过del语句删除不再使用的变量。
​	如果对象没有被变量引用，就会被垃圾回收器回收清空内存空间。

## 常量

​	Python实际上不支持常量，即没有语法规则限制修改一个常量的值。通常只能常量的命名规则，以及在程序的逻辑上不对常量的值作出修改。

## 链式赋值

​	链式赋值用于同一个对象赋值给多个变量。

```python
x = y = 100
```

## 序列解包赋值

```python
a,b,c = 1,2,3
```

## 同一运算符

​	同一运算符用于比较两个对象的存储单元，实际比较的是对象的地址。
​	is 用于判断两个标识符是不是引用同一个对象。
​	is not 是判断两个标识符是不是引用不同对象。

### is与==的区别

- is 用于比较两个变量引用对象是否为同一个，即比较对象的地址。
- == 用于判断引用变量引用对象的值是否相等，默认调用对象的`_eq()_`方法。

## 整数缓存问题

- 命令行模式下，Python仅仅会对较小的整数对象进行缓存（范围为[-5,256]），用数组实现，分配连续空间，便于查找，而非所有整数对象。
- 文件模式下，所有数字都会被缓存，范围是：[-∞,+∞]。[-5,256]仍然使用数组实现，不在[-5,256]出现的数，缓存在链表中，不分配连续空间。

## 字符串

 	Python的**字符串是不可变的**，无法对原字符做任何修改。但是可以将字符串的一部分复制到新创建的字符串，达到看起来修改的效果。

## 转义字符

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250630112354373.png" alt="image-20250630112354373" style="zoom:45%;" />

## 字符串拼接

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250630112922913.png" alt="image-20250630112922913" style="zoom:50%;" />



## 从控制台读取字符串

​	可以使用`input（）`从控制台读取键盘输入的内容。

## Replace()实现字符串替换

​	字符串不可改变。需要替换某些字符时，只能通过创建新的字符串实现。

```python
a = 'abcd'
# 将字符b换成字符a
b = a.replace('b','a')
print(b)
```

## 使用[]提取字符

- 字符串的本质就是字符序列，可以通过在字符串后面添加[]，在[]里面指定偏移量，可以提取该位置的单个字符。

  - 正向搜索

    最左侧第一个字符，偏移量是0，第二个偏移量是1，直到`len(str)-1`为止。

  - 反向搜索

    最右侧第一个字符，偏移量是-1，第二个偏移量是-2，直到`-len(str)-1`为止。

## 字符串切片slice操作

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250630115337017.png" alt="image-20250630115337017" style="zoom:50%;" />

##  split()分割和join()合并

- split()可以基于指定分割符将字符串分割成多个子字符串并存储到列表中。如果不指定分割符，则默认使用**空白字符**（换行符/空格/制表符）
- join()用于将一系列字符串连接起来。

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250630124628598.png" alt="image-20250630124628598" style="zoom:50%;" />

```python
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
```

## 字符串驻留机制

- 字符串驻留：常量字符串只保留一份

```python
c = 'dd#@'
d = 'dd#@'
print(c is d) #True
```

##  字符串格式化

```python
# 字符串格式化
a = '姓名:{0},年龄:{1}'
b = a.format('joe','22')
print(b)

c = '姓名:{name},年龄:{age}'
d = c.format(name='Jack',age='11')
print(d)
```

## 数字格式化

- 浮点数通过f，整数通过d进行需要的格式化

```python
# 数字格式化
a = '{:.2f}'
print(a.format(3.1415))
```

## 可变字符串

```python
import io 
s = 'abcdefg' # s仍然不可变
sio = io.StringIO(s) # sio就是可变字符串
print(sio)
print(sio.getvalue())
sio.seek(3) #指针到索引3这个位置
sio.write("@@")
print(sio.getvalue())

```

## 列表

- 用于存储任意数量、任意类型的数据集合
- 列表是内置可变序列，是包含多个元素的有序连续的内存空间。
- 列表中的元素类型可以各不相同，大小可变，可以根据需要随时增加或者删除。

##  元组

- 元组属于不可变序列，不能修改元组中的元素。
- 元组的访问和处理速度比列表快。
- 与整数和字符串一样，元组可以作为字典的键，而列表不能作为字典的键。

## 生成器推导式创建元组

```python
a = (i for i in range(10)) # 生成器对象
b = tuple(a)
print(b) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

- 生成器对象只能使用一次，如果需要重新访问其中的元素，必须重新创建该生成器对象。

```python
c = (i for i in range(3))
print(c.__next__()) # 1
print(c.__next__()) # 2
print(c.__next__()) # 3
```

- `__next__()`方法实现对生成器对象的遍历。









































