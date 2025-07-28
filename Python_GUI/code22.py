
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x150")

def test1():
    with askopenfile(title="上传文件",initialdir='/',filetypes=[("文本文件",".txt")]) as f:
        show['text'] = f.read()
Button(root,text="选择需要读取的文本文件",command=test1).pack()

show = Label(root,width=40,height=3,bg="yellow")
show.pack()

root.mainloop()
