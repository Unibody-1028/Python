# def add(a:int,b:int,c:int)->int:
#     '''实现三个整数的相加，并返回它们的和'''
#     sum = a+b+c
#     print('它们的和是：'+str(sum))
#     return sum

# add(1,2,3)
# #查看函数信息
# help(add)
# print(add.__doc__)

# def print_star(n:int):
#     print("*"*n)
# c = print_star
# c(3)


# 局部变量和全局变量效率测试

# import time 
# a = 100
# def test01():
#     global a 
#     start = time.time()
#     for i in range(100000000):
#         a += 1
#     end = time.time()
    
#     print("耗时：{}".format(end-start))
    
# def test02():
#     a = 100
#     start = time.time()
#     for i in range(100000000):
#         a += 1
#     end = time.time()
    
#     print("耗时：{}".format(end-start)) 
    

# test01()
# test02()


# def f1(a,b,*c):
#     print(a,b,c)
    
# f1(1,2,3,4)

# def f2(a,b,**c):
#     print(a,b,c)
    
# f2(1,2,x=3,y=4)

#匿名函数
# f = lambda x,y,z : x+y+z
# print(f(1,2,3))

# g = [lambda x:x*2,lambda y:y*3,lambda z:z*4]
# print(g[0](2),g[1](3),g[2](4))

#测试eval（）函数
# s = "print('abc')"
# eval(s)


#递归
# def f1(n):
#     print("start:"+str(n))
#     if n==1:
#         print("recursion over!")
#     else:
#         f1(n-1)
#     print('end:'+str(n))
    
# f1(3)    

# #阶乘
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


#嵌套函数

# def outer():
#     print('outer running')
#     def inner():
#         print('inner running')
#     inner()

# outer()

# def printName(isChinese,name,familyName):
#     def inner_print(a,b):
#         print("{0} {1}".format(a,b))
#     if isChinese:
#         inner_print(familyName,name)
#     else:
#         inner_print(name,familyName)
        
# printName(True,'力','田')
# printName(False,'Geroge','Bush')

#测试nonlocal、global关键字的用法
# a = 100
# def outer():
#     b = 10
    
#     def inner():
#         nonlocal b # 声明使用外部函数的局部变量
#         print("inner b:",b)
#         b = 20
        
#         global a # 声明全局变量
#         a = 1000
        
#     inner()
#     print('outer b',b)
    
# outer()
# print('outer a',a)

# class Student:
    
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
        
    
#     def print_score(self):
#         print(self.score)

# s1 = Student("Jack",100)
# s1.print_score()


# class Student:
#     def say_hello(self):
#         print(self,'----','hello')
        
# s1 = Student()
# s1.say_hello()
# Student.say_hello(s1)

# class Student:
#     company = "Aniplex"
#     count = 0
    
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#         Student.count = Student.count+1
#     def say_score(self):
#         print("我的公司是：",Student.company)
#         print(self.name,"的分数是：",self.score)
        
# s1 = Student('Jack',80)
# s2 = Student('Ben',90)

# s1.say_score()
# print("一共创建了{}个Student对象".format(Student.count))



# class Student:
#     company = "Aniplex"
    
#     @classmethod
#     def printCompany(cls):
#         print(cls.company)
#     @staticmethod
#     def add(a,b):
#         print("{0}+{1}={2}".format(a,b,(a+b)))
#         return a+b
        
# Student.printCompany()
# Student.add(30,40)


#自定义call（）函数
# class Car:
#     def __call__(self,age,price):
#         print("车龄{0},价格{1}".format(age,price))
        
# c1 = Car()

# c1(8,10000)


# #测试方法的动态性
# class Person:
#     def work(self):
#         print("努力上班")

# def play_game(self):
#     print("玩游戏")
# def work2(self):
#     print("好好工作，努力上班")
# Person.work = work2
# Person.play = play_game
# p = Person()
# p.work()
# p.play()

#测试私有属性、私有方法
# class Employee:
#     __company = "Aniplex" #解释器运行时，把__company转成了_Employee__company
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def print_info(self): 
#         print("我的公司是",Employee.__company)
#         print("我的年龄是",self.__age)
#     def __work(self):
#         print("努力工作") 
        
        
        
# print(dir(Employee))
# print(Employee._Employee__company)
# a = Employee('jack',20)
# a.print_info()
# a._Employee__work()
# print(a._Employee__age)


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
#     @property
#     def salary(self):
#         print('薪资是：',self.__salary)
#         return self.__salary
#     @salary.setter
#     def salary(self,salary):
#         self.__salary = salary

# emp1 = Employee('Jack',10000)
# emp1.salary 
# emp1.salary=20000
# emp1.salary


# class Person:
#     def __init__(self,name,age):
#         print("创建Person")
#         self.name = name
#         self.age = age
        
#     def print_age(self):
#         print("{0}的年龄是{1}".format(self.name,self.age))
     
     
# class Student(Person):
#       def __init__(self, name, age, score):
#           #调用父类的构造方法
#           #Person.__init__(self,name,age)
#           super(Student,self).__init__(name,age)         
#           print("创建Student")
#           self.score = score
        
# s1 = Student('Jack',20,100)
# s1.print_age()

# class Person():
#     def __init__(self,name):
#         self.name = name
    
# class Student(Person):
#     def __init__(self,name):
#         Person.__init__(self,name)
#         #super(Student,self).__init__(name)

# s1 = Student("Jack")
# print(s1.name)

# obj = object()
# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#     def say_age(self):
#         print(self.name,"的年龄是",self.age)
    
# s1 = Person("jack",20)
# print(dir(s1))

#重写str方法 
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         '''将对象转化为一个字符串，一般用于print方法'''
#         print("重写__str__方法")
#         return "名字是{0},年龄是{1}".format(self.name,self.age)
    
# p = Person("jack",20)
# print(p)

# s = str(p)
# print(s)
        
# class A():
#     def aa(self):
#         print('aa')
#     def say(self):
#         print("say AAA")
        
        
# class B():
#     def bb(self):
#         print('bb')
#     def say(self):
#         print("say BBB")
        
        
# class C(A,B):
#     def cc(self):
#         print('cc')

# c = C()
# print(C.mro())
# c.say()


# class A:
#     def __init__(self):
#         print("A的构造方法")
        
#     def say(self):
#         print("A:",self)     
#         print("AAA")
        
    
# class B(A):
#     def __init__(self):
#         A.__init__(self)    # 调用父类的构造方法
#         #super(B,self).__init__()
#         print("B的构造方法")
#     def say(self):          #调用父类的say()方法
#         A.say(self)     
#         #super().say()
#         print("B:",self)
#         print("BBB")

# b = B()        
# b.say()



# class Animal:
#     def shout(self):
#         print('动物叫了一声')


# class Dog(Animal):
#     def shout(self):
#         print('小狗汪汪汪')
        
        
# class Cat(Animal):
#     def shout(self):
#         print("小猫喵喵喵")
        
# def animalshout(a):
#     a.shout()    #根据传入的对象不同，调用的方法也不一样。
    
# a = Animal()
# b = Dog()
# c = Cat()

# l1 = [a,b,c]
# for i in l1:
#     animalshout(i)

# a = 20
# b = 30
# c = a+b
# d = a.__add__(b)
# print("c:",c)
# print("d:",d)

# #测试运算符的重载
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __add__(self,other):
#         if isinstance(other,Person):
#             return "{0}--{1}".format(self.name,other.name)
#         else:
#             return "不是同类对象，不能相加"

#     def __mul__(self,other):
#         if isinstance(other,int):
#             return self.name*other
#         else:
#             return "不是同类对象，不能相乘"
    
# p1 = Person('Jack')
# p2 = Person('Ben')

# print(p1+p2)
# print(p1*3)

# #拷贝测试
# import copy
# class MobilePhone():
#     def __init__(self,CPU):
#         self.CPU = CPU
    
# class CPU:
#     pass

# c = CPU()
# m = MobilePhone(c)
# print("浅拷贝")
# m2 = copy.copy(m)
# print("m:",id(m))
# print("m2:",id(m2))
# print("m中的CPU：",id(m.CPU))
# print("m2中的CPU：",id(m2.CPU))

# print('----------------------')
# print("深拷贝")
# m2 = copy.deepcopy(m)
# print("m:",id(m))
# print("m2:",id(m2))
# print("m中的CPU：",id(m.CPU))
# print("m2中的CPU：",id(m2.CPU))

# #组合
# class CPU:
#     def calculate(self):
#         print("正在计算")
        
# class Screen:
#     def show(self):
#         print("正在显示")

# class MobilePhone:
#     def __init__(self,cpu,screen):
#         self.cpu = cpu
#         self.screen = screen
# c = CPU()
# s = Screen()
# m = MobilePhone(c,s)
# m.cpu.calculate()
# m.screen.show()

# #工厂模式
# class Benz:
#     pass
# class BMW:
#     def __init__(self):
#         print('BMW')
# class BYD:
#     pass

# class CarFactory:
#     def createCar(self,brand):
#         if brand == '奔驰':
#             return Benz()
#         elif brand == '宝马':
#             return BMW()
#         elif brand == "比亚迪":
#             return BYD()
#         else:
#             return "未知品牌"

# fac = CarFactory()
# car1 = fac.createCar('宝马')

# #单例模式
# class MySingleton:
#     __obj = None
#     __init_flag = True
    
#     def __new__(cls,*args,**kwargs):
#         if cls.__obj == None:
#             cls.__obj = object.__new__(cls)
#         return cls.__obj
        
#     def __init__(self,name):
#         if MySingleton.__init_flag:
#             print('初始化第一个对象......')
#             self.name = name
#             MySingleton.__init_flag = False
            
# a = MySingleton('aa')
# print(a)
# b = MySingleton('bb')
# print(a)   

# #工厂模式和单例模式结合
# class Benz:
#     pass
# class BWM:
#     pass
# class BYD:
#     pass
# class Factory:
#     __obj = None
#     __init_flag = True
    
#     def __new__(cls,*args,**kwargs):
#         if cls.__obj == None:
#             cls.__obj = object.__new__(cls)
#         return cls.__obj
        
#     def __init__(self):
#         if Factory.__init_flag:
#             Factory.__init_flag = False
    
#     def createCar(self,brand):
#         if brand == "奔驰":
#             return Benz()
#         elif brand == "宝马":
#             return BWM()
#         elif brand == "比亚迪":
#             return BYD()
#         else:
#             print('未知品牌')
            
# factory = Factory()
# c1 = factory.createCar('奔驰')
# c2 = factory.createCar('宝马')

# print(c1)   
# print(c2)   

# factory2 = Factory()      

# print(factory)
# print(factory2)
            