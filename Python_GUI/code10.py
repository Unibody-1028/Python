"""测试grid布局管理器"""
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """通过布局管理器实现登陆界面"""
        self.label01 = Label(self,text="用户名")
        self.label01.grid(row=0,column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0,column=1)
        Label(self,text="用户名为手机号").grid(row=0,column=2)

        Label(self,text="密码").grid(row=1,column=0)
        Entry(self,show="*").grid(row=1,column=1)

        Button(self,text="登陆").grid(row=2,column=1,sticky=EW)
        Button(self,text="取消",command=root.destroy).grid(row=2,column=2,sticky=W)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600+300+300")
    app = Application(master=root)
    root.mainloop()