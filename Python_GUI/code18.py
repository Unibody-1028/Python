"""OptionMenu的使用测试"""
from tkinter import *

root = Tk()
root.geometry("200x100")
v = StringVar(root)
v.set("鸡")
om = OptionMenu(root,v,"狗","猫","鸭","牛")
om['width'] = 10
om.pack()


def test1():
    print("最喜欢的动物：",v.get())
 
Button(root,text="确定",command=test1).pack()

root.mainloop()
