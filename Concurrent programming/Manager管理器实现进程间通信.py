from multiprocessing import Manager,Process

def func(name,m_list,m_dict):
    m_list.append("你好")
    m_dict["name"] = "Jack"


if __name__ == '__main__':
    with Manager() as mgr:
        m_list = mgr.list()
        m_dict = mgr.dict()
        m_list.append("Hello")

        # 两个进程间不能直接互相使用对象，需要互相传递
        p1 = Process(target=func,args=("p1",m_list,m_dict))
        p1.start()
        p1.join()
        print(f"主进程{m_dict}")
        print(f"主进程{m_list}")


