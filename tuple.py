#chứa mọi giá trị, là một container
#giống list

my_tuple = ("aabc", 'b', 'a', 'd', 1,23,4)

print(my_tuple.count('a'))

print(my_tuple.index('a'))

tup = (i for i in range(10) if i % 2 == 1)

a = tuple('hoana2007')
b = tuple(tup)
c = a+b
print(b)
print(a)
print(c)
d = a[:-1]
print(d)