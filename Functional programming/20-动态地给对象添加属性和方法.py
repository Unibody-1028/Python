import types


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("A",20)
p2 = Person("B",30)

# 动态的给对象添加属性和方法
p1.score = 100
print(p1.score)

def run(self):
    print(f"{self.name},running")

# 将p1和run函数进行绑定
p1.run = types.MethodType(run,p1)
p1.run()


