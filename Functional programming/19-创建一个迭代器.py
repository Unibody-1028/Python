# 创建一个依次返回10,20,30,...这样数字的迭代器
class MyNumbers:
    def __iter__(self):
        self.name = 10
        return self

    def __next__(self):
        while True:
            x = self.name
            self.name += 10
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
