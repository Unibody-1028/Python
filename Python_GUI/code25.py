"""通用消息框"""
from tkinter import  *
from tkinter.messagebox import *

root = Tk()
root.geometry("400x200")

a1 = showinfo(title="Python",message="学Python")
print(a1)# 打印ok
root.mainloop()

