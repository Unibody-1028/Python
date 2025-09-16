class Person:
    pass
@staticmethod
def staticfunc():
    print("this is a static method")
Person.staticmethod = staticfunc
Person.staticmethod()

@classmethod
def classfunc(cls):
    print("this is a class method ")
    print(f"i am {cls.__name__}")
Person.classmethod = classfunc
Person.classmethod()


# 添加属性
Person.score = 100
print(Person.score)