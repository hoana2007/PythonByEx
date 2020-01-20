count = 0
n = 0
while (count < 8):
    print("so thu",n," la: ", count)
    n += 1
    count +=1
print("ket thuc")

#input day gi
n = int(input("Nhap n = "))
tong = 0
i = 1
while i <= n:
    tong = tong + i
    i += 1

print("Tong tinh duoc la: ", tong)

#whil ma lai co else
dem = 0
while dem < 5:
    dem = dem + 1
    print(dem)
else:
    print("Cho nay la else")


bien = 10 
while bien > 0: 
    print ('Giá trị biến hiện tại là: ', bien) 
    bien = bien -1 
    if bien == 5: 
        break 
    print ("OK!")