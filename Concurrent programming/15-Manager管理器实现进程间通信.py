from multiprocessing import Manager,Process

def func(name,m_list,m_dict):
    m_list.append("你好")
    m_dict["name"] = "Jack"


if __name__ == '__main__':
    """
    核心作用说明
        进程间数据共享：普通的列表 / 字典无法在多进程间共享（子进程修改后，主进程看不到变化），
        而 Manager 创建的 mgr.list() 和 mgr.dict() 是跨进程共享的，子进程对它们的修改会被主进程感知到。
    执行结果：
        主进程先向 m_list 添加 "Hello"。
        子进程 p1 启动后，向 m_list 添加 "你好"，向 m_dict 添加 {"name": "Jack"}。
        子进程结束后，主进程打印的共享数据会包含子进程的修改，因此最终输出包含两者的操作结果。
"""



    # 创建一个Manager上下文，用于管理共享数据
    with Manager() as mgr:
        # 通过Manager创建共享列表和字典（跨进程可见）
        m_list = mgr.list()
        m_dict = mgr.dict()

        # 主进程先向共享列表添加一个元素
        m_list.append("Hello")

        # 创建子进程p1，目标函数是func，传递参数（进程名、共享列表、共享字典）
        p1 = Process(target=func, args=("p1", m_list, m_dict))
        p1.start()  # 启动子进程
        p1.join()  # 等待主进程等待子进程执行完毕

        # 子进程执行后，主进程打印共享字典和列表的内容
        print(f"主进程{m_dict}")  # 输出：主进程{'name': 'Jack'}
        print(f"主进程{m_list}")  # 输出：主进程['Hello', '你好']


