import time 
import random

# 九九乘法表
# for x in range(1,10): 
#     for y in range(1,x+1):
#         print(x,"x",y,'=',x*y,end='\t')   
#     print()
    
# while True:
#     a = input('请输入一个字符（输入Q/q以结束）')
#     if a.upper() == 'Q':
#         break
#     else:
#         print(a)


# 循环代码优化测试
# start = time.time()
# for i in range(1000):
#     result = []
#     for m in range(10000):
#         c = i * 1000
#         result = result + [c+m*100]    
# end = time.time()
# print("耗时：{0}".format(end-start))

# print('代码优化后------')
# start2 = time.time()
# for i in range(10000):
#     result = []
#     c = i * 1000
#     for m in range(1000):
#         result.append(c+m*100)
# end2 = time.time()
# print("耗时：{0}".format(end2-start2))  
    

# import turtle
# p = turtle.Pen()
# radius = [x*10 for x in range(1,11)]
# my_colors = ['red','blue','yellow','black','green']
# p.width(4)

# for r,i in zip(radius,range(len(radius))):
#     p.penup()
#     p.goto(0,-r)
#     p.pendown()
#     p.color(my_colors[i%len(my_colors)])
#     p.circle(r)
    
# turtle.done()

# import turtle
# width = 30
# num = 18
# x1 = [(-400,400),(-400+width*num,400)]
# y1 = [(-400,400),(-400,400-width*num)]

# t = turtle.Pen()
# t.speed(10)

# for i in range(num+1):
#     t.penup()
#     t.goto(x1[0][0],x1[0][1]-30*i)
#     t.pendown()
#     t.goto(x1[1][0],x1[1][1]-30*i)




