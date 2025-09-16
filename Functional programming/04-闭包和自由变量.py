# # 全局变量实现a自增，但会污染全局变量
# a = 10
# def add():
#     global a
#     a += 1
#     print("a:",a)
#
# def print_ten():
#     if a == 10:
#         print("a == 10")
#     else:
#         print("a != 10")
# add()
# add()
# add()
# print_ten()
#
# # 局部变量实现，但是不能实现自增
#
# def add():
#     a = 10
#     a += 1
#     print("a:",a)
#
# def print_ten():
#     if a == 10:
#         print("a == 10")
#     else:
#         print("a != 10")
# add()
# add()
# add()
# print_ten()

# 通过自由变量实现自增，且不污染全局变量
a = 10
print("---------------")
def add():
    a = 10
    def increment():
        nonlocal a
        a += 1
        print("a:",a)
    return increment

def print_ten():
    if a == 10:
        print("a == 10")
    else:
        print("a != 10")
a1 = add()
a1()
a1()
a1()
a1()
print_ten()


