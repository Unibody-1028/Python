"""测试Checkbutton按钮"""
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master) # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()
        print(self.codeHobby.get()) # 默认是0

        self.c1 = Checkbutton(self,text="敲代码",variable=self.codeHobby,onvalue=1,offvalue=0)
        self.c2 = Checkbutton(self,text="看视频",variable=self.videoHobby,onvalue=1,offvalue=0)

        self.c1.pack(side="left")
        self.c2.pack(side="left")

        Button(self,text="确定",command=self.confirm).pack(side="bottom")




    def confirm(self):
        if self.codeHobby.get() == 1:
            messagebox.showinfo(message="我是程序猿")
        if self.videoHobby.get() ==1:
            messagebox.showinfo(message="我喜欢刷短视频")




if __name__ =='__main__':
    root = Tk()
    root.geometry("800x600+300+300")
    app = Application(master=root)
    #root.wm_attributes("-topmost",True)
    root.mainloop()