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

