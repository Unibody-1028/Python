# 语句结构
'''
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
'''

status = 404
match status:
    case 200:
        print("访问成功")
    case 404:
        print("页面不存在")
    case _:
        print("unknown error")

p1 = ("Jack",22,'male')
p2 = ("Anna",24,'female')
p3 = ("Zoe",21,None)
def func(person):
    match person:
        case (name,_,"male"):
            print(f"{name} is male")
        case (name, _, "female"):
            print(f"{name} is female")
        case (name,age,gender):
            print(f"{name},{age},{gender}")
func(p1)
func(p2)
func(p3)