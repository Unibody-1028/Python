"""测试Radiobutton按钮"""
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __int__(self,master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()


    def createWidget(self):
        # 变量v存放Radiobutton选中的值
        self.v = StringVar()
        # 变量v初始化为F，并且Radiobutton默认选择value="F"的选项
        self.v.set("F")

        self.r1 = Radiobutton(self,text="男性",value="M",variable=self.v)
        self.r2 = Radiobutton(self,text="女性",value="F",variable=self.v)

        #组件左对齐
        self.r1.pack(side="left")
        self.r2.pack(self="left")
        Button(self,text="确定",command=self.confirm).pack(side="left")


    def confirm(self):
        messagebox.showinfo("测试",message="选择的性别"+self.v.get())



if __name__ =='__main__':
    root = Tk()
    root.geometry("800x600+300+300")
    app = Application(root)
    root.wm_attributes("-topmost",True)
    root.mainloop()