a = id(10)
print(a)
n = 70
print(n)
print(n + 1)
print(n.__add__(5))
print(n.__radd__(5))
print(-n)
print(n.__neg__())

s1 = "HKteam"
s2 = "Free"
print(id(s1))
print(id(s2))

s1 = s1 + 'python'
s2 += 'python'
print(id(s1))
print(id(s2))

a1 = [1,2]
a2 = [3,4]
print(id(a1))
print(id(a2))

a1 = a1 + [0]
a2 += [0]

print(id(a1))
print(id(a2))