import pandas as pd
import matplotlib.pyplot as plt


#Doc du lieu tu Excel
from pandas import ExcelFile
hs_path = 'H:\Python\PythonByEx\PythonByEx\k12.xlsx'
df = pd.read_excel(hs_path)

print("Nhan phim bat ky de dong")

plt.subplot(2,2,1)
plt.plot(df["Toan"], color = "red")
plt.xlabel("Loai diem")
plt.ylabel("So luong")
plt.title("DIEM TOAN")

plt.subplot(2,2,3)
dulieu = [1,2,3]
tencot = ["A","B","C"]
plt.bar(tencot, dulieu, color = "green")
plt.xlabel("Loai diem")
plt.ylabel("So luong")
plt.title("DIEM TOAN")

plt.subplot(2,2,2)
h = [0,1,2,3,4,5,6,7,8,9,10]
plt.ylim(0,10)
plt.xlim(0,10)
plt.scatter(df["Toan"], df["Toan"], color = "green")
plt.xlabel("Loai diem")
plt.ylabel("So luong")
plt.title("DIEM TOAN")

plt.show()