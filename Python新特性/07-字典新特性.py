data = {"a":1,"b":2,"c":3}
print("字典:",data)
# keys，values,items
print("items:",data.items())
print("values:",data.values())
print("keys:",data.keys())
print("\n")

# 新特性,使用keys，values,items获取字典的原数据
keys = data.keys()
values = data.values()
items = data.items()

print(keys.mapping)
print(values.mapping)
print(items.mapping)
print("\n")

# 旧版本
keys = ["name","age"]
values = ["Jack",22]
data_dict = dict(zip(keys,values))
print(data_dict)
# 新版本
keys = ["name","age"]
values = ["Jack",22,21]
data_dict2 = dict(zip(keys,values,strict=True))
print(data_dict2)



