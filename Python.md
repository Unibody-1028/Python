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

## 字典

- 字典是“键值对”的无序可变序列，字典中的每一个元素都是一个“键值对”，包含“键对象”和“值对象”。可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。
- “键”是任意的不可变数据，可变对象不能作为“键”。
- “键不可重复”，“值”可以是任意数据且可以重复。 

### 创建字典

1. 通过`{}`和`dict{}`创建字典对象。

   ```python
   # 字典
   a = {'name':'Jack','age':18}
   b = dict(name='Jack',age=18)
   c = dict([('name','Jack'),('age',18)])
   d = {}
   e = dict()
   ```

2. 通过zip()创建字典对象。

   ```python
   k = ['name','age','job']
   v = ['Jack',18,'programmer']
   d = dict(zip(k,v))
   print(d)
   ```

3. 通过formkeys创建值为空的字典。

```python
f = dict.fromkeys(['name','age','job'])
print(f)
```

##  字典用法总结

1. 字典在内存中的开销巨大，典型的空间换时间。
2. 键查询速度很快。
3. 往字典里添加新键可能导致扩容，导致散列表中的次序变化。因此不要在遍历字典的同时进行字典的修改。
4. 键必须可散列
   - 数字、字符串、元组都是可散列的
   - 自定义对象需要支持如下三点：
     - 支持`hash()`函数
     - 支持通过`__eq__()`方法检测相等性
     - 若`a==b`为真，则`hash(a)==hash(b)`也为真。

## 集合

​	集合无序可变，元素不能重复。集合底层使用字典实现，集合的所有元素都是字典的键对象，因此不能重复且唯一。



## 循环代码优化

1. 尽量减少循环内部不必要的计算。
2. 嵌套循环中，尽量减少内部循环的计算，尽可能向外提。
3. 局部变量查询较快，尽量使用局部变量。

其它优化手段：

1. 连接多个字符串，使用`join()`而不使用+。
2. 列表进行插入和删除，尽量在列表尾部操作。

```python
# 循环代码优化测试
start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        c = i * 1000
        result = result + [c+m*100]    
end = time.time()
print("耗时：{0}".format(end-start))

print('代码优化后------')
start2 = time.time()
for i in range(10000):
    result = []
    c = i * 1000
    for m in range(1000):
        result.append(c+m*100)
end2 = time.time()
print("耗时：{0}".format(end2-start2))  
```

## 推导式创建序列

​	推导式是从一个或者多个迭代器快速创建序列的一种方法。它可以将循环和条件判断结合从而避免冗长的代码。

 语法：

```python
[表达式 for item in 可迭代对象]
或者：[表达式 for item in 可迭代对象 if 条件判断]
```

## 函数

1. 函数是可重用的代码块。
2. 函数不仅可以实现代码的复用，更能实现代码的一致性，即只要修改函数的代码，则所有调用该函数的地方都能得到体现。

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250702092319915.png" alt="image-20250702092319915" style="zoom:50%;" />

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250702092442861.png" alt="image-20250702092442861" style="zoom:40%;" />

1. 变量c和print_star都指向了同一个函数对象。因此执行c()和print_star()的效果完全一致。
2. Python中圆括号意味着调用函数，在没有圆括号的情况下，Python会把函数当作普通对象。

## 变量

### 全局变量：

1. 在函数和类定义之外的变量。作用域为定义的模块，从定义位置开始直到模块结束。
2. 全局变量降低了函数的通用性和可读性。应尽量避免全局变量的使用。
3. 要在函数内改变全局变量的值，使用`global`声明一下。

### 局部变量：

1. 在函数体中声明的变量（包含形参）。
2. 局部变量的引用比全局变量快，优先考虑使用。
3. 如果局部变量和全局变零同名，则在函数内隐藏全局变量，只使用同名的局部变量。

## 参数传递

1. 函数的参数传递本质上就是：从形参到实参的赋值操作。
2. Python中一切都是对象，赋值操作都是引用的赋值。

**具体操作时分为两类**

1. 对可变对象进行写操作，直接作用于原对象本身，包括字典、列表、集合、自定义的对象等。
2. 对不可变对象进行写操作，会产生一个新的对象空间，并用新的值填充这块空间，包括数字、字符串、元组、function等。

## 浅拷贝和深拷贝

​	**浅拷贝**：拷贝对象，但不拷贝子对象的内容，只是拷贝子对象的引用。

​	**深拷贝**：拷贝对象，并且会将子对象的内容拷贝一份，对拷贝对象的修改不会影响源对象。

<img src="/Users/guopengpeng/Library/Application Support/typora-user-images/image-20250702103240742.png" alt="image-20250702103240742" style="zoom:50%;" />

## 参数传递：不可变对象包含可变对象

​	传递不可变对象时，不可变对象里面包含的子对象是可变的，对子对象进行修改，源对象也会发生变化。

## 可变参数

1. *param，将多个参数收集到一个元组中。
2. **param，将多个参数收集到一个字典中。（必须使用强制命名参数）

## Lambda函数

​	lambda表达式可以用来声明匿名函数，实际上生成了一个函数对象。

```python
lambda arg1,arg2,arg3...:  <表达式>
```

​	arg1 arg2 arg3 为函数的参数。<表达式>相当于函数体。运算结果是表达式的运算结果。

## eval()函数

​	将字符串`str`当作有效的表达式求值并返回计算结果。

​	eval(source, globals,locals)

​	**参数：**

1. source:一个Python表达式或者函数compile()返回的代码对象。
2. globals:可选，必须是字典。
3. Locals:可选，任意映射对象。

​	**eval()函数会将字符串当作语句执行，因此会有安全隐患。**

