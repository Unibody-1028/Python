"""测试Label组件的基本用法，使用面向对象的方式"""
from tkinter import *


class Application(Frame):
    """一个经典的GUI程序的类的写法"""
    def __init__(self, master=None):
        super().__init__(master)            # super()代表父类的定义，而不是父类对象
        self.master = master

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """创建组件"""
        self.label01 = Label(self,text="这是一个Label组件",width=20,height=4,
                             bg="black",fg="white",font=("SimHei",10))
        self.label01.pack()

        self.label02 = Label(self, text="这是第二个Label组件", width=20, height=4,
                             bg="blue", fg="white",font=("",10))
        self.label02.pack()

        # 显示图像
        global photo  # 将photo声明为全局变量，局部变量在本方法执行完毕后会被销毁。
        photo = PhotoImage(file="image/doro.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        # 多行文本
        self.label04 = Label(self,text="多行文本的第一行\n多行文本的第二行\n多行文本的第三行\n",
                             borderwidth=1, # 边框宽度
                             relief="solid", # 设置组件的3D样式
                             justify="center", # 文本内容居中
                             height=5,    # 增加高度容纳多行文本
                             wraplength=400, # 设置自动换行宽度
                             bg="lightgray" # 设置背景色使其更加明显
                             )
        self.label04.pack()

if __name__=='__main__':

    root = Tk()
    root.geometry('1200x800+150+100')
    # 将窗口置顶
    root.wm_attributes("-topmost", True)
    app = Application(master=root)
    root.mainloop()







