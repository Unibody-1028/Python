"""测试canvas组件的基本用法"""
import random
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        self.canvas = Canvas(self,width=600,height=400,bg="green")
        self.canvas.pack()
        # 画一条直线(折线，每一对坐标是一个点，左手系，左上角坐标为（0，0）)
        line = self.canvas.create_line(0,10,20,20,30,50)

        # 画一个矩形
        rect = self.canvas.create_rectangle(50,50,100,100)

        # 画一个椭圆，两个坐标为椭圆边界矩形的左上角和右下角
        oval = self.canvas.create_oval(50,50,100,100)

        global photo
        photo = PhotoImage(file="./image/doro.gif")
        self.canvas.create_image(220,220,image=photo)

        # 绘制矩形
        Button(self,text="画10个矩形",command=self.draw50Recg).pack(side="left")

        # 退出按钮
        Button(self,text="退出",command=root.destroy).pack(side="left")



    def draw50Recg(self):
        for i in range(10):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width'])/2)
            y2 = y1 + random.randrange(int(self.canvas['height']) / 2)

            self.canvas.create_rectangle(x1,y1,x2,y2)
        messagebox.showinfo(message="绘制成功")

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600+300+300")
    app = Application(master=root)
    root.mainloop()
