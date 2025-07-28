# 测试command属性绑定事件，测试lambda表达式传参

from tkinter import *
root = Tk()
root.geometry("800x600")

def mouseTest1():
    print("command方式，简单情况；不涉及获取event对象")

def mouseTest2(a,b):
    print("a={0},b={1}".format(a,b))
Button(root,text="测试command1",
       command=mouseTest1).pack(side="left")
Button(root,text="测试command2",
       command=lambda :mouseTest2("111","222")).pack(side="left")

root.mainloop()