# 对list进行升序排序
sorted1 = sorted([1,-2,6,-5,10,5])
print("升序排序",sorted1)

# sorted函数实现自定义排序
sorted2 = sorted([1,3,6,-20,-70],key=abs)
print("按绝对值大小升序排序",sorted2)

sorted3 = sorted([1,3,6,-20,-70],key=abs,reverse=True)
print("按绝对值大小降序排序",sorted3)

# 按照ASCII排序
sorted4 = sorted(["ABC","abc","B","D"])
print("字符串排序",sorted4)

# 按照忽略大小写排序
sorted5 = sorted(["ABC","abc","B","D"],key=str.lower)
print("忽略字符串大小写排序",sorted5)

# 按照忽略大小写反向排序
sorted6 = sorted(["ABC","abc","B","D"],key=str.lower,reverse=True)
print("忽略字符串大小写排序",sorted6)






