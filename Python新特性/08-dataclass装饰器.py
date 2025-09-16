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


