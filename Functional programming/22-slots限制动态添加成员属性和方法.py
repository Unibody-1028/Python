class Person:
    __slots__={"name","age"} # 限制实例只能有 name 和 age 属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("吃饭")
if __name__ == '__main__':
    p1 = Person("Jack",18)
    #p1.gender = "man"
    p1.eat()