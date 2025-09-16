def test1():
    print("test1 function running")
def test2(func):
    print("test2 function running")
    func()

if __name__ == '__main__':

    print(test1)
    print(type(test1))
    a = test1
    a()
    print(a is test1)

    test2(a) # a作为参数传递给test2()
