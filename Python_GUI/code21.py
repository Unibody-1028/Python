"""文件对话框选择文件"""
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x150")

def test1():
    f = askopenfilename(title="上传文件",
                        initialdir='/',filetypes=[("文本文件",".txt")])
    show['text'] = f
Button(root,text="选择Python文件",command=test1).pack()

show = Label(root,width=40,height=3,bg="yellow")
show.pack()

root.mainloop()
