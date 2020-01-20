print("heng")

for i in 'com':
    print('ky tu: ',i)

hoten = ["bo", "me", "anh", "em"]
for ten in hoten:
    print(ten)

#cho dayx so
A = [1,5,3,7]
#sap xep
A.sort()
print(A)
#tong cac phan tu trong A
tong = 0 
for i in A:
    tong += i

print("Tong = ", tong)

#su dung ham range
B = list(range(20))
print(B)

#dem so chan trong B
demchan = 0;
demle = 0;
for j in B:
    if j%2 == 0:
        demchan += 1
    else: demle += 1

print("so luong so chan la: ", demchan)
print("so luong so le la:",demle)
