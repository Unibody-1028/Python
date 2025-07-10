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
