"""简单对话框"""
from tkinter import  *
from tkinter.simpledialog import *

root = Tk()
root.geometry("400x200")
def test1():
    a = askinteger(title="输入年龄",prompt="请输入年龄",initialvalue=18,minvalue=1,maxvalue=128)
    show['text'] = a
Button(root,text="你的年龄是？请输入",command=test1).pack()

show = Label(root,width=40,height=3,bg="yellow")
show.pack()

root.mainloop()
