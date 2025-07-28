"""测试Text多行文本框组件的基本用法"""
from tkinter import *
import webbrowser

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)     # super()代表父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.w1 = Text(root,width=40,height=20,bg="gray")
        self.w1.pack()

        self.w1.insert(1.0,"12345\nabcdefg") # 在第1行第1列放入字符
        self.w1.insert(3.1,"风华绝代\n") # 在第3行第2列放入字符



if __name__ == "__main__":
    root = Tk()
    # 设置窗口位置和大小
    root.geometry("800x640+300+300")
    app = Application(root)
    root.wm_attributes("-topmost",True)
    root.mainloop()
