"""测试Entry组件"""
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """登陆界面的组件"""
        self.label01 = Label(self,text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件
        # StringVar变量的值发生变化时，组件内容也会相应改变；如果组件内容改变，则StringVar也随之改变
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get())
        print(self.entry01.get())



        # 创建密码框
        self.label02 = Label(self,text="密码")
        self.label02.pack()
        v2 = StringVar()
        self.entry02 = Entry(self,textvariable=v2,show="*")
        self.entry02.pack()

        # 登陆按钮
        self.btn01 = Button(self, text="登陆", command=self.login)
        self.btn01.pack()

    def login(self):
        print("用户名:"+self.entry01.get())
        print("密码:" + self.entry02.get())
        messagebox.showinfo(message="系统登陆成功")
        messagebox.showinfo(message="用户名:"+self.entry01.get())

if __name__ == "__main__":
    root = Tk()
    # 设置窗口位置和大小
    root.geometry("800x640+300+300")
    app = Application(master=root)
    root.wm_attributes("-topmost", True)
    root.mainloop()

