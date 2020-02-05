a = "Nguyen Anh Hòa"
b = a.split(' ',2)
print(a)
print(b)
c = a.partition('An')
print(type(c))

d = a.count('n')
print(d)

#bắt đầu bằng kí tự gì?
e = a.startswith('N')
print(e)

f = a.find('n', 0, 7)
print(f)

h = a.isupper()
print(h)