# try:
#     print('step1')
#     a = 3/0
#     print('step2')
# except BaseException as e:
#     print('step3')
#     print(e)
# print('step4')
# print('step5')
 
# while True:
#     try:
#         x = int(input("请输入一个数字："))
#         print("您输入的数字是:",x)
#         if x == 88:
#             print('退出程序')
#             break
#     except BaseException as e:
#         print(e)

# try:
#     a = input("请输入被除数:")
#     b = input("请输入除数:")
#     c = float(a)/float(b)
#     print(c)
# except ZeroDivisionError:
#     print("除数不能为零")
# except ValueError:
#     print("除数和被除数都应该是数值类型")
# except BaseException as e:
#     print(e)
    
# try:
#     a = input("请输入被除数:")
#     b = input("请输入除数:")
#     c = float(a)/float(b)
# except BaseException as e:
#     print(e)
# else:
#     print("除法结果为:",c)
# finally:
#     print('无论是否发生异常，我都会被执行。')
#print("程序结束")    

# try:
#     f = open('/Users/guopengpeng/Python/Python_Advanced/a.txt',"r")
#     content = f.readlines()
#     print(content)
# except BaseException as e:
#     print(e)
# finally:
#     print('关闭文件')
#     f.close()
# print('继续执行其他代码') 
# print('程序结束')

# with上下文管理器
# with open('/Users/guopengpeng/Python/Python_Advance/a.txt',"r") as f:
#     for line in f:
#         print(line)

# #traceback模块
# import traceback
# try: 
#     print('step1')
#     num = 1/0
# except:
#     with open('/Users/guopengpeng/Python/Python_Advance/log.txt','a') as f:
#         traceback.print_exc(file=f)
        
# #自定义异常类
# class AgeError(Exception):
#     def __init__(self,errorInfo):
#         Exception.__init__(self)
#         self.errorInfo = errorInfo
#     def __str__(self):
#         return str(self.errorInfo)+"，年龄错误！应该在1-150之间"
    
# if __name__ == '__main__':#如果是True，则模块是作为独立文件执行，这下面可以写测试代码
#     age = int(input('输入一个年龄：'))
#     if(age<1 or age>150):
#         raise AgeError(age)
#     else:
#         print('年龄正常：',age)
        
  
# print(2**16)

# try:
#     f = open(r'log.txt','r')
#     for i in f.readlines():
#         print(i,end='\t')
# except BaseException as e:
#     print(e)
# finally:
#     f.close()


    
# s = ['百度','阿里','腾讯']

# with open('b.txt',encoding='utf-8',mode='a') as f:
#     f.writelines(s)
    
#为文本文件每一行的末尾增加行号
# with open('b.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     # print(lines)   
#     lines2 = [line.rstrip()+" #"+str(index)+"\n" for  index,line in zip(range(1,len(lines)+1),lines)]
#     print(lines2)
# with open("c.txt",'a',encoding='utf-8')as f:
#     f.writelines(lines2)

# #使用pickle实现序列化和反序列化
# import pickle
# with open('data.dat','wb') as f:
#     score = [1,2,3]
#     pickle.dump(score,f)

# with open('data.dat','rb') as f:
#     score2 = pickle.load(f)
#     print(score2)

# #读取CSV文件
# import csv
# with open('a.csv') as f:
#     a_csv = csv.reader(f) #创建csv对象，它是一个包含所有数据的列表，每一行为一个元素
#     headers = next(a_csv) #获得列表对象，包含标题行的信息
#     print(headers)
#     print('----------')
#     for row in a_csv: #循环打印各行内容
#         print(row)


# #写入csv文件
# headers = ['name','age','salary']
# rows = [('Anna',22,12000),('David',24,10000)]
# with open('b.csv','w') as f:
#     b_csv = csv.writer(f)  #创建csv对象
#     b_csv.writerow(headers)#写入一行(标题)
#     b_csv.writerows(rows)  #写入多行(内容)


# import os
# # windows计算器
# # os.system('Calc.exe')
# # mac计算器
# # os.system('open /System/Applications/Calculator.app')
# # ping 百度
# # os.system("ping www.baidu.com")

# print(os.name)
# print(os.sep)
# print(repr(os.linesep)) #repr可以显示数据信息

# a = '3'
# print(a)
# print(repr(a))
# #获取文件和文件夹的相关信息
# print(os.stat('pycode1.py'))
# #关于工作目录的操作
# print(os.getcwd()) #获得当前的工作目录

# #改变当前的工作目录
# os.chdir('/Users/guopengpeng/Python/Python_Advance')

# #创建、删除目录
# os.mkdir('1')
# os.rmdir('1')

# #创建多级目录
# if not os.path.exists('电影/港台/周星驰'):
#     os.makedirs('电影/港台/周星驰')
    
# #修改目录名
# os.rename('电影','movie')
# #列出子目录
# print(os.listdir('movie'))
# #删除多级目录
# os.removedirs('movie/港台/周星驰')


# # 测试os.path常用方法

# import os
# import os.path
# # 获得当前目录
# path = os.getcwd()
# file_list = os.listdir(path) # 列出子目录和子文件
# print(file_list)
# # 取出.py文件
# for file_name in file_list:
#     if os.path.splitext(file_name)[1] == '.py':
#         print(file_name)

# # 推导式列出目录下的所有.py文件    
# file_list2 = [file_name for file_name in os.listdir(path) if file_name.endswith('.py')]
# print(file_list2)

# # walk()递归遍历所有文件和目录
# import os
# path = os.getcwd()
# list_files = os.walk(path,topdown=False) #False表示先遍历子目录

# for root,dirs,files in list_files: #root表示当前遍历的目录,dirs表示root目录下的子目录,files表示root目录下的文件
#     for file_name in files:
#         print(os.path.join(root,file_name)) #打印文件
#     for dir_name in dirs: 
#         print(os.path.join(root,dir_name))  #打印目录


# 实现文件的拷贝
# import shutil
# shutil.copyfile('a.txt','a_copy.txt')


# # 递归遍历目录树
# import os

# def my_print_file(path,level):
#     child_files = os.listdir(path) #先获取path路径下的所有文件和目录列表
#     # 遍历获取到的文件和目录列表
#     for file in child_files:
#         # 将获取到的文件或目录与根目录拼接并打印
#         file_path = os.path.join(path,file)
#         print("\t"*level+file_path[file_path.rfind(os.sep)+1:])
#         # 再次判断已经打印出的变量是否为目录
#         if os.path.isdir(file_path):
#             # 如果是目录，则继续查看子目录
#             my_print_file(file_path,level+1)

# my_print_file('电影',1)

        
# import math
# help(math) 

import salary
print(salary.__doc__)
print(salary.__name__)



