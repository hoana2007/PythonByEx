list = ["apple","banana", "potato", "leman", "orange"]
print(list)

print(list[2])

print(list[-2])

print(list[-4:-1])

list[1] = "qua Oi"
print(list)

for i in list:
	print(i+"   hoa qua")

if "apples" in list:
	print("dung")

x = len(list)
print(x)

list.append("pipe")
print(list)


list.insert(3,"carrot")
print(list)

list.pop()
print(list)

del list[1]
print(list)

print("----------------------")
#del list
#list.clear()
list2 = list.copy()
print("Danh sach 2: ")
print(list2)

list3 = list + list2
print(list3)

list4 = [1,2,3,4,5]
for x in list4:
    list.append(x)

print(list)

list5 = list(("a","b","c","d"))
print(list5)