def mylog(type):
    def decorator(func):
        def infunc(*args,**kwargs):
            if type == "文件":
                print("文件中：日志记录")
            else:
                print("控制台：日志记录")
            return func(*args,**kwargs)
        return infunc
    return decorator


@mylog("文件")
def fun2():
    print("使用功能2")

if __name__ == '__main__':
    fun2()

