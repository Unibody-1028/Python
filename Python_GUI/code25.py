"""开发记事本软件的菜单"""
from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)     # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.textpad = None         # textpad表示Text文本框对象
        self.pack()
        self.createWidget()
        

    def createWidget(self):
        # 创建主菜单栏                          
        menubar = Menu(self.master)

        #  创建子菜单栏
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)",menu=menuFile)
        menubar.add_cascade(label="编辑(E)",menu=menuEdit)
        menubar.add_cascade(label="帮助(H)",menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建",accelerator="control+n",command=self.test)
        menuFile.add_command(label="打开",accelerator="control+o",command=self.test)
        menuFile.add_command(label="保存",accelerator="control+s",command=self.test)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="退出",accelerator="control+q",command=root.destroy)

        # 将主菜单栏加到根窗口
        root['menu'] = menubar

        # 文本编辑区
        self.textpad = Text(self,width=50,height=30)
        self.textpad.pack()
        
        # 创建上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色",command=self.test)
        
        # 为右键绑定事件，绑定到文本框
        self.textpad.bind("<Button-2>",self.createContextMenu)

    def test(self):
        pass
    
    def createContextMenu(self,event):
        # 菜单在鼠标右键单击的坐标处显示
        self.contextMenu.post(event.x_root,event.y_root)

if __name__ == '__main__':
    root = Tk()
    root.geometry("450x300+300+300")
    root.title("简易记事本")
    app = Application(master=root)
    root.mainloop()