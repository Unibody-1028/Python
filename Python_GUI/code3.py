"""测试一个经典的GUi程序的写法，使用面向对象的方式"""
from tkinter import messagebox
from tkinter import *


class Application(Frame):
    """一个经典的GUI程序的类的写法"""
    def __init__(self, master=None):
        super().__init__(master)            # super()代表父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.btn01 = None
        self.btnQuit = None
        self.createWidgets()

    def createWidgets(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "按钮"
        self.btn01.pack()
        self.btn01["command"] = self.printInfo

        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def printInfo(self):
        messagebox.showinfo("打印信息","正在打印信息！") # macos不允许显示标题


if __name__=='__main__':

    root = Tk()
    root.geometry('1000x800+300+150')
    root.title("一个经典的GUI程序类的测试")
    # 将窗口置顶
    root.wm_attributes("-topmost", True)
    app = Application(master=root)

    root.mainloop()







