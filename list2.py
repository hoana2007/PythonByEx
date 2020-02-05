#khởi tạo list
a = [i for i in range(25)]
print(a[24])

b = [[n, n*1, n*2] for n in range(1,4)]
print(b)

c = [1,2,3]
d = list(c)
print(c)
print(d)
d[0] = 'abc'
print(d)
print(c)

e = [1,2,3,4,5,6]
f = e.count(2)
#copy f = e.copy()
e.insert(1,4)
print(e)
