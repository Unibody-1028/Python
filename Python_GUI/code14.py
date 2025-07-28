""""扑克牌游戏的界面设计"""
from cProfile import label
from tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过place布局管理器实现扑克牌位置控制"""
        # self.photo = PhotoImage(file="image/puke/puke1.gif")
        # self.puke1 = Label(self.master,image=self.photo)
        # self.puke1.place(x=10,y=10)
        self.photos = [PhotoImage(file="image/puke/puke"+str(i+1)+".gif") for i in range(10)]
        self.pukes = [Label(self.master,image=self.photos[i])for i in range(10)]

        for i in range(10):
            self.pukes[i].place(x=10+i*30,y=10)
        # 为所有的Label增加事件处理
        self.pukes[0].bind_class("Label","<Button-1>",self.chupai)

    def chupai(self,event):
        print(event.widget.winfo_geometry())
        #print(event.widget.winfo_x())
        if event.widget.winfo_y() == 10:
            event.widget.place(y=0)
        else:
            event.widget.place(y=10)

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x210+300+300")
    app = Application(master=root)
    root.mainloop()

