
dictx = {
    "ho": "Nguyễn",
    "ten": "Hòa",
    "Nam_sinh":1983
    }
print(dictx)

x = dictx["ho"] ##x = dictx.get("ho")
print(x)

dictx["ten"] = "Hiếu"
print(dictx)

for i in dictx:
    print(i,"    ",dictx[i])

for y in dictx.values():
    print(y)


for n,m in dictx.items():
    print(m,n)

if "ho" in dictx:
    print("dung")

print(len(dictx))

dictx["Que_quan"] = "Yên Lập"
print(dictx)

#dictx 1

dictx1 = dictx.copy()
print(dictx1)


family = {
    "bố":{
        "surname": "Nguyễn",
        "tên": "Hòa"
        },
    "mẹ":{
        "surname": "Lâm",
        "tên": "Liên"
        },
    "con 1":{
        "surname": "Nguyễn",
        "tên": "Hiếu"
        },
    "con 2":{
        "surname": "Nguyễn",
        "tên": "Lan"
        }
    }

print(family)

