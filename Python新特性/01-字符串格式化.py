name = "jack"
age = 20
print("姓名:%s,年龄:%d"%(name,age))

print("姓名:{},年龄:{}".format(name,age))

print(f"姓名:{name},年龄:{age}")

names = ["a","b","c"]
print(f"字符串1:{names[0]},字符串2:{names[1]},字符串3:{names[2]}")

a = 10
b = 20
print(f"a+b={a+b}")

print("-"*40)

a = 10
b = 20
print(f"{a=},{b=}")
# 使用指定的字符居中显示
name = "TTT"
print("{:*^20}".format(name))
print(f"{name:*^20}")
# 居左显示
print(f"{name:*<20}")
# 居右显示
print(f"{name:*>20}")

# 对数值变量的格式化
price =3.1415
print("{:.2f}".format(price))
print(f"{price:.2f}")

num = 12
print(f"{num=:.1f}")

pct = 0.789
print("{:.2f}%".format(pct*100))
print(f"{pct*100:.0f}%")
print(f"{pct*100:.1f}%")
print(f"{pct*100:.2f}%")

print("-"*40)
s = "HelloWorld"
print(s.removeprefix("Hello"))  # 输出："World"（移除前缀"Hello"）
print(s.removeprefix("Hi"))     # 输出："HelloWorld"（无匹配前缀，返回原字符串）

s2 = "test_test.py"
print(s2.removeprefix("test_"))  # 输出："test.py"（移除前缀"test_"）

s = "HelloWorld"
print(s.removesuffix("World"))  # 输出："Hello"（移除后缀"World"）
print(s.removesuffix("Bye"))    # 输出："HelloWorld"（无匹配后缀，返回原字符串）

s2 = "document.txt"
print(s2.removesuffix(".txt"))  # 输出："document"（移除后缀".txt"）