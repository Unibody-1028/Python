# 未使用线程同步和互斥锁
from threading import Thread
from time import sleep


class Account:
    def __init__(self,name,money):
        self.name = name
        self.money = money

# 模拟提款操作
class Drawing(Thread):
    def __init__(self,drawingNum,account):
        # 调用父类初始化函数
        super().__init__()
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0
    def run(self):
        if self.account.money<self.drawingNum:
            return
        sleep(1) # 测试冲突问题
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum

        print("账户名:{},余额:{}".format(self.account.name,self.account.money))
        print("账户名:{},总共取出金额为:{}".format(self.account.name,self.expenseTotal))

if __name__ == '__main__':
    a1 = Account("Jack",100)
    draw1 = Drawing(80,a1) # 第一个取钱的线程
    draw2 = Drawing(100,a1)
    # 启动线程
    draw1.start()
    draw2.start()
