# Python3.6之前不加.abc
from collections.abc import Iterator
from collections.abc import Iterable
# 判断list类型
a = isinstance([],Iterable)
print(a)

b = isinstance([],Iterator)
print(b)

c = isinstance(iter([]),Iterator)
print(c)

d = isinstance(iter([]),Iterator)
print(d)

