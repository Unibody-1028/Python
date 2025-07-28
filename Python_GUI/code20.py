"""askcolor颜色选择框的测试"""
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry("400x200")

def test1():
    s1 = askcolor(color="white",title="选择背景色")
    print(s1)
    root.config(bg=s1[1])

Button(root,text="选择背景色",command=test1).pack()
root.mainloop()