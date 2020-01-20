# import module sys để gọi ra các ngoại lệ
import sys

randomList = ['a', 0, 2]

for nhap in randomList:
 try:
   print("Phần tử:", nhap)
   r = 1/int(nhap)
   break
 except: 
     print("Có ngoại lệ ",sys.exc_info()[0]," xảy ra.") 
     print("Nhập phần tử tiếp theo")
     print()
print("Kết quả với phần tử",nhap,"là:",r)
