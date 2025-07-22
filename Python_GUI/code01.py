from tkinter import *
from tkinter import messagebox


root = Tk() # 创建窗口对象
root.title('我的第一个GUI程序') # 设置标题
root.geometry('1000x800+400+150') # 设置

btn01 = Button(root) # 创建一个Button对象，放入到窗口对象
btn01['text'] = '这是一个按钮'
btn01.pack()

def func1(e):  # e就是事件对象
    messagebox.showinfo('Message','这是一个函数')
    print('打印信息')

btn01.bind('<Button-1>',func1)

root.mainloop() # 调用组件的mainloop()方法，进入事件循环

