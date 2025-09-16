import functools


def int2(x,base=2):
	return int(x,base)
print(int2("1000")) #8
print(int2("111"))  #7

int2 = functools.partial(int,base = 2)
print(int2("1010")) #10
print(int2("1011")) #11
print(int2("1010",base = 10))

