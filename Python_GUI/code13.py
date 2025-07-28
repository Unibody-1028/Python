# coding=utf-8
from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("place布局管理器")
root['bg'] = "white"

f1 = Frame(root,width=200,height=200,bg="green")
f1.place(x=30,y=30)

# relx或rely 和(x,y)同时存在时，(x,y)相当于relx/rely基础上的偏移量
Button(root,text="Class").place(relx=0.1,x=100,y=50,relwidth=0.5,relheight=0.5)
Button(root,text="Jack").place(relx=0.2,rely=0.2)
Button(root,text="Jack").place(relx=0.3,rely=0.3)
Button(root,text="Jack").place(relx=0.4,rely=0.4)
Button(root,text="Ben").place(relx=0.5,rely=0.5)



root.mainloop()