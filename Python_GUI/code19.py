"""Scale滑块的使用测试"""
from tkinter import *

root = Tk()
root.geometry("400x300")

def test1(value):
    print("滑块的值为：",value)
    newFont = ("宋体",value)

    # 调整字体大小
    a.config(font=newFont)


s1 = Scale(root,from_=5,to=25,length=250,tickinterval=2,orient="horizontal",command=test1)
s1.pack()
a = Label(root,text="Hello World!",width=15,height=2,bg="grey",fg="blue")
a.pack()

root.mainloop()