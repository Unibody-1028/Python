'''
元类：
    什么是元类？
    动态创建类
    元类->类

    类->对象

    用途？
        可以动态创建类
    type()
        1.查看目标对象的数据类型
        2.动态创建类
        语法:类 = type(类名,(父类...),{属性、方法})
'''

# 创建一个默认父类，不包含任何属性方法的类
Person = type('Person',(),{})
p1 = Person()
# print(p1)
# # mro() 查找父类
# print(Person.mro())
class Animal:
    def __init__(self,color):
        self.color = color
    def eat(self):
        print("eating")
def sleep(self):
    print("sleeping")

# 使用type动态创建一个类，继承Animal
Dog = type('Dog',(Animal,),{"age":1,"sleep":sleep})
dog1 = Dog("Black")
dog1.sleep()
dog1.eat()
print(dog1.color)

