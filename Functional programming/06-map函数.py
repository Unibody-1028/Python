def f(x):
    return x**2
list1 = [1,2,3,4,5]
L = map(f,list1)
print(list(L))

L = map(lambda n:n**2 ,list1)
print(list(L))

def f2(x,y):
    return x+y
L = map(f2,[1,2,3],[10,20,30,40])
print(list(L))

L = map(lambda x,y : x+y, [1,2,3], [10,20,30,40])
print(list(L))