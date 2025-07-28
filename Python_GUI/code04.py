"""测试Button组件的基本用法，使用面向对象的方式"""
from tkinter import *
from tkinter import messagebox


class Appcication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(root,text="登陆",command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file="image/doro.gif")
        self.btn02 = Button(root,image=photo,command=self.login)
        self.btn02.pack()
        # self.btn02.config(state="disabled") #设置按钮的状态


    def login(self):
        messagebox.showinfo(title="标题",message="系统登陆成功")



if __name__ == "__main__":
    root = Tk()
    root.geometry("800x640+200+300")
    app = Appcication(master=root)
    # 将窗口置顶
    root.wm_attributes("-topmost", True)
    root.mainloop()

