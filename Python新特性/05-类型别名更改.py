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