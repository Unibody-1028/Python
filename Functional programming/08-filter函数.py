# 删除list的偶数，保留奇数
def is_odd(n):
    return n % 2 == 1
L = filter(is_odd,[1,2,3,4])
print(list(L)) # [1, 3]

L = filter(lambda n:n%2==1,[1,2,3,4,5])
print(list(L)) # [1, 3, 5]

# 删除空字符串
def not_empty(s):
    return s and s.strip()
L = filter(not_empty,["A",""," ",None,"ABC"])
print(list(L))

L = filter(lambda s:(s and s.strip()) , ["A",""," ",None,"ABC"])
print(list(L))

