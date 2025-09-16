dict1 = {'name':"Jack"}
dict2 = {'age':22}
# 旧版本
dict1.update(dict2)
print("dict1:",dict1)
print("dict2:",dict2,"\n")

# 新版本
dict1 = {'name':"Jack"}
dict2 = {'age':22}
dict3 =dict1|dict2
print("dict1:",dict1)
print("dict2:",dict2)
print("dict3:",dict3,"\n")

# 更新字典
dict1 = {'name':"Jack"}
dict2 = {'age':22}
dict1 |= dict2 # 等价于dict1 = dict1 | dict2
print("dict1:",dict1)
print("dict2:",dict2)
