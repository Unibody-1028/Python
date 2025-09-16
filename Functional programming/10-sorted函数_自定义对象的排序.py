from functools import cmp_to_key


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 自定义排序方法
def custom_sorted(stu1,stu2):
    if stu1.age < stu2.age:
        return -1
    if stu1.age > stu2.age:
        return 1
    return 0

stu1 = Student('a',20)
stu2 = Student('b',30)
stu3 = Student('c',40)
stu4 = Student('d',50)

student_list = sorted([stu4,stu3,stu2,stu1],key=lambda x: x.age)
for stu in student_list:
    print(f"学生姓名:{stu.name},学生年龄:{stu.age}")

print("---------------------------------------------")

student_list = sorted([stu4,stu3,stu2,stu1],key=lambda x: x.age,reverse=True)
for stu in student_list:
    print(f"学生姓名:{stu.name},学生年龄:{stu.age}")

print("---------------------------------------------")

student_list = sorted([stu4,stu3,stu2,stu1],key=cmp_to_key(custom_sorted))
for stu in student_list:
    print(f"学生姓名:{stu.name},学生年龄:{stu.age}")
