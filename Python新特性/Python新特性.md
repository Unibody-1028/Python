# 字符串格式化

## 1. 旧式字符串格式化（`%` 占位符）

```
name = "jack"
age = 20
print("姓名:%s,年龄:%d"%(name,age))  # 输出：姓名:jack,年龄:20
```

- 原理：使用 `%` 作为占位符，后面跟**格式字符**表示变量类型，最后用 `%` 连接变量元组。
- 常用格式字符：
    - `%s`：字符串（可接收任何类型，自动转为字符串）。
    - `%d`：整数。
    - `%f`：浮点数（如 `%.2f` 表示保留 2 位小数）。
- 特点：Python 早期的格式化方式，兼容性好，但对于复杂场景（如多参数、嵌套）语法较繁琐。

## 2. `str.format()` 方法

```
print("姓名:{},年龄:{}".format(name,age))  # 输出：姓名:jack,年龄:20
```

- 原理：使用 `{}` 作为占位符，通过 `format()` 方法传入变量，按顺序填充占位符。
- 进阶用法：
    - 可以指定索引：`"姓名:{0},年龄:{1},再次姓名:{0}".format(name, age)`（`0` 表示第一个参数，`1` 表示第二个）。
    - 可以指定参数名：`"姓名:{n},年龄:{a}".format(n=name, a=age)`。
- 特点：比 `%` 方式更灵活，支持复杂格式化（如对齐、填充、精度控制），适用于 Python 3.0+。

## 3. f-string（格式化字符串字面值，Python 3.6+）

```
print(f"姓名:{name},年龄:{age}")  # 输出：姓名:jack,年龄:20
```

- 原理：在字符串前加 `f` 或 `F`，直接在 `{}` 中嵌入变量名，运行时自动替换为变量值。
- 特点：
    - 简洁直观，变量直接写在字符串中，可读性强。
    - 支持在 `{}` 中写表达式（见下面的例子）。
    - 性能优于 `%` 和 `format()`，是 Python 3.6 后的推荐用法。

## 4. f-string 进阶用法（嵌入表达式 / 索引）

```
# 示例1：嵌入列表索引
names = ["a","b","c"]
print(f"字符串1:{names[0]},字符串2:{names[1]},字符串3:{names[2]}")  
# 输出：字符串1:a,字符串2:b,字符串3:c

# 示例2：嵌入算术表达式
a = 10
b = 20
print(f"a+b={a+b}")  # 输出：a+b=30
```

- f-string 支持在 `{}` 中直接写**表达式**（如列表索引 `names[0]`、算术运算 `a+b`），运行时会计算表达式结果并嵌入字符串。
- 这是 f-string 最强大的特性之一，避免了先计算再传参的繁琐。



# Python 字符串格式化（f-string 与 format 方法）总结

## 一、变量名与值同时输出（f-string 特有）

```
a = 10
b = 20
print(f"{a=},{b=}")  # 输出：a=10,b=20
```

- 语法：`f"{变量名=}"`
- 作用：直接输出「变量名 = 值」的格式，简化调试时的打印逻辑。

## 二、字符串对齐与填充

通过指定宽度和填充字符，实现字符串的居中、居左、居右对齐（`format` 与 f-string 通用）。



| 对齐方式 | 语法（format）           | 语法（f-string） | 示例（name="TTT"）                        |
| -------- | ------------------------ | ---------------- | ----------------------------------------- |
| 居中     | `"{:*^20}".format(name)` | `f"{name:*^20}"` | `********TTT*********`（总宽 20，* 填充） |
| 居左     | `"{:*<20}".format(name)` | `f"{name:*<20}"` | `TTT*****************`                    |
| 居右     | `"{:*>20}".format(name)` | `f"{name:*>20}"` | `*****************TTT`                    |

- 说明：
    - `*` 为填充字符（可替换为任意字符，如 `#`、空格等）；
    - `20` 为总宽度（字符串长度 + 填充字符数 = 20）；
    - `<`（左对齐）、`>`（右对齐）、`^`（居中）为对齐符号。

## 三、数值格式化

对数字（整数、浮点数、百分比等）进行精度控制或格式转换。

### 1.**浮点数精度控制**

```
price = 3.1415
print("{:.2f}".format(price))  # 输出：3.14（保留2位小数）
print(f"{price:.2f}")          # 输出：3.14（同上）
```

- 语法：`:.nf`（`n` 为保留的小数位数）。

### 2.**变量名 + 精度组合（f-string 特有）**

```
num = 12
print(f"{num=:.1f}")  # 输出：num=12.0（变量名+1位小数）
```



### 3.**百分比格式**

```
pct = 0.789  # 0.789 即 78.9%
print("{:.2f}%".format(pct*100))  # 输出：78.90%（保留2位小数）
print(f"{pct*100:.0f}%")          # 输出：79%（无小数位，四舍五入）
print(f"{pct*100:.1f}%")          # 输出：78.9%（保留1位小数）
```

- 原理：先将小数乘以 100，再用 `%` 符号拼接，配合精度控制实现百分比显示。

# 字符串新方法

## 1. `str.removeprefix(prefix)`

- **功能**：如果字符串以指定的 `prefix` 开头，则移除该前缀并返回新字符串；如果字符串不以 `prefix` 开头，则返回原字符串（不修改）。
- **参数**：`prefix` 为要移除的前缀字符串（必须是字符串类型）。
- **特点**：仅移除**最前面**的匹配前缀，且**只移除一次**。

```
s = "HelloWorld"
print(s.removeprefix("Hello"))  # 输出："World"（移除前缀"Hello"）
print(s.removeprefix("Hi"))     # 输出："HelloWorld"（无匹配前缀，返回原字符串）

s2 = "test_test.py"
print(s2.removeprefix("test_"))  # 输出："test.py"（移除前缀"test_"）
```

## 2. `str.removesuffix(suffix)`

- **功能**：如果字符串以指定的 `suffix` 结尾，则移除该后缀并返回新字符串；如果字符串不以 `suffix` 结尾，则返回原字符串（不修改）。
- **参数**：`suffix` 为要移除的后缀字符串（必须是字符串类型）。
- **特点**：仅移除**最后面**的匹配后缀，且**只移除一次**。

```
s = "HelloWorld"
print(s.removesuffix("World"))  # 输出："Hello"（移除后缀"World"）
print(s.removesuffix("Bye"))    # 输出："HelloWorld"（无匹配后缀，返回原字符串）

s2 = "document.txt"
print(s2.removesuffix(".txt"))  # 输出："document"（移除后缀".txt"）
```

# 变量类型标注

​	变量类型注解是用来对变量和函数的参数返回值类型做注解，帮助开发者写出更严谨的代码，让调用方减少类型方面的错误，提高代码的可读性和易用性。

## 一、简单类型变量标注

直接在变量名后加 `:类型` 标注基本数据类型：

| 类型标注 | 说明   | 示例代码              |
| -------- | ------ | --------------------- |
| `int`    | 整数   | `a: int = 10`         |
| `str`    | 字符串 | `b: str = "hello"`    |
| `float`  | 浮点数 | `c: float = 3.14`     |
| `bool`   | 布尔值 | `d: bool = True`      |
| `bytes`  | 字节串 | `e: bytes = b"Hello"` |

- 作用：明确变量的预期类型，帮助开发者和工具理解代码逻辑。
- 检查工具：安装 `mypy` 后，通过 `mypy 文件名.py` 可进行类型校验（如变量赋值与标注类型不符时会报错）。

## 二、复杂类型变量标注（容器类型）

对于列表、集合、字典、元组等容器类型，需使用 `typing` 模块中的类型工具（Python 3.10 之前需手动导入，3.10+ 可直接使用内置泛型）。

| 容器类型       | 标注方式                   | 说明                                       | 示例代码                                    |
| -------------- | -------------------------- | ------------------------------------------ | ------------------------------------------- |
| 列表（List）   | `List[元素类型]`           | 指定列表中所有元素的类型                   | `x: List[int] = [1, 2, 3]`                  |
| 集合（Set）    | `Set[元素类型]`            | 指定集合中所有元素的类型                   | `y: Set[str] = {"a", "b"}`                  |
| 字典（Dict）   | `Dict[键类型, 值类型]`     | 分别指定字典的键和值的类型                 | `z: Dict[str, int] = {'a': 1, 'b': 2}`      |
| 元组（Tuple）  | `Tuple[类型1, 类型2, ...]` | 按位置指定元组中每个元素的类型（固定长度） | `m: Tuple[int, str, bool] = (1, "a", True)` |
| 元组（可变长） | `Tuple[元素类型, ...]`     | 所有元素为同一类型，长度可变               | `Z: Tuple[int, ...] = (1, 2, 3, 4)`         |

## 三、注意事项

1. **兼容性**：
    - Python 3.5 及以上支持基本类型标注。
    - Python 3.10 引入 **`list[int]`、`dict[str, int]`** 等简化写法，无需导入 `typing` 模块（与 `List[int]` 等效）。
2. **非强制性**：
    类型标注仅为 “提示”，Python 解释器不会强制执行（即使类型不符也能运行），但静态检查工具（如 `mypy`）会报错。
3. **适用场景**：
    - 大型项目中提升代码可读性和协作效率。
    - 配合 IDE（如 PyCharm）实现自动补全和错误提示。

通过类型标注，可使代码逻辑更清晰，尤其在团队协作或复杂项目中，能有效减少类型相关的 bug。

# 函数参数和返回值类型标注

## 一、普通函数的类型标注

为函数参数和返回值指定类型，明确输入输出的预期类型：

```
def add1(x: int, y: int) -> int:
    return x + y
```

- 语法：`参数名: 类型` 标注参数类型；`-> 类型` 标注返回值类型。
- 示例中，`x` 和 `y` 被标注为 `int`（整数），函数返回值也为 `int`。
- 作用：通过 `mypy` 等工具可检查参数类型是否匹配（如传入字符串会报错）。

## 二、函数变量的类型标注（`Callable`）

当变量指向函数时，使用 `Callable` 标注函数的参数类型和返回值类型：

```
from typing import Callable

# 标注：变量 f 指向一个接收 (int, int) 参数、返回 int 的函数
f: Callable[[int, int], int] = add1
```

- 语法：`Callable[[参数类型1, 参数类型2, ...], 返回值类型]`。
- `[int, int]` 表示函数接收两个 `int` 类型参数；`int` 表示返回值类型。
- 适用场景：变量存储函数、函数作为参数传递时，明确函数的签名（参数和返回值类型）。

## 三、生成器的类型标注（`Iterator`）

生成器函数的返回值需标注为 `Iterator[元素类型]`，接收生成器的变量也需对应标注：

```
from typing import Iterator

# 生成器函数：返回值标注为 Iterator[int]（生成整数的迭代器）
def return_num(num: int) -> Iterator[int]:
    i = 0
    while i < num:
        yield i  # 生成 int 类型元素
        i += 1

# 变量标注：与生成器返回值类型一致（Iterator[int]）
b: Iterator[int] = return_num(5)
for i in b:
    print(i)  # 输出 0,1,2,3,4
```

- 生成器本质是迭代器，因此返回值类型标注为 `Iterator[T]`（`T` 为生成元素的类型）。
- 接收生成器的变量需标注为相同的 `Iterator[T]`，确保类型匹配。

# 混合类型检查改进

```
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
```

# 类型别名更改

```
# 旧版本
oldname = str
def oldfunc(param:oldname)->oldname:
    return param + param
print(oldfunc("Hello!"))


# 新版本
from typing import TypeAlias
newname:TypeAlias = str
def newfunc(param:newname)->newname:
    return param + param
print(newfunc("Hello!"))
```

# 统计二进制数字中“1”的个数

```
# 旧版本
value1 = 5
print(bin(value1).count("1"))

# 新版本
# bit_count()函数
print(value1.bit_count())
```

# 字典新特性

## 字典的三个方法新增mapping属性

```
data = {"a":1,"b":2,"c":3}
print("字典:",data)
# keys，values,items
print("items:",data.items())
print("values:",data.values())
print("keys:",data.keys())
print("\n")

# 新特性,使用keys，values,items获取字典的原数据
keys = data.keys()
values = data.values()
items = data.items()

print(keys.mapping)
print(values.mapping)
print(items.mapping)
```

##  zip函数新增strict参数

```python
# 旧版本
keys = ["name","age"]
values = ["Jack",22]
data_dict = dict(zip(keys,values))
print(data_dict)
# 新版本
keys = ["name","age"]
values = ["Jack",22,21]
# 需要keys,values严格对齐
data_dict2 = dict(zip(keys,values,strict=True)) 
print(data_dict2)
```

# dataclass装饰器

```
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Player:
    name:str
    age:int
p1 = Player("Jack",22)
print(p1)
print("\n")

@dataclass
class Player:
    name:str
    age:int
    # file设置默认值
    gender:str = field(default='male',repr=False)
    msg:str = field(default="")
    # 设置类属性
    Country:ClassVar[str]

p1 = Player("Jack",22)
print(p1)
Player.country = "中国"
print(Player.country)
```

# 字典合并

```
dict1 = {'name':"Jack"}
dict2 = {'age':22}
# 旧版本
dict1.update(dict2)
print("dict1:",dict1)
print("dict2:",dict2,"\n")

# 新版本
dict1 = {'name':"Jack"}
dict2 = {'age':22}
dict3 =dict1|dict2
print("dict1:",dict1)
print("dict2:",dict2)
print("dict3:",dict3,"\n")

# 更新字典
dict1 = {'name':"Jack"}
dict2 = {'age':22}
dict1 |= dict2 # 等价于dict1 = dict1 | dict2
print("dict1:",dict1)
print("dict2:",dict2)

```

# match语法

```
# 语句结构
'''
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
'''

status = 404
match status:
    case 200:
        print("访问成功")
    case 404:
        print("页面不存在")
    case _:
        print("unknown error")

p1 = ("Jack",22,'male')
p2 = ("Anna",24,'female')
p3 = ("Zoe",21,None)
def func(person):
    match person:
        case (name,_,"male"):
            print(f"{name} is male")
        case (name, _, "female"):
            print(f"{name} is female")
        case (name,age,gender):
            print(f"{name},{age},{gender}")
func(p1)
func(p2)
func(p3)
```









































