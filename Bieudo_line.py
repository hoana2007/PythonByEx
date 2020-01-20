import pandas as pd
import matplotlib.pyplot as plt


#Doc du lieu tu Excel
from pandas import ExcelFile
hs_path = 'H:\Python\PythonByEx\PythonByEx\k12.xlsx'
df = pd.read_excel(hs_path)

print(df["Toan"])


plt.subplot(2,2,1)
plt.plot(df["Toan"], color = "c")
plt.ylabel("loại điểm")
plt.xlabel('Số lượng')
plt.title('TRUNG BÌNH TOAN')

plt.subplot(2,2,2)
plt.plot(df["Van"], color = "red") #, "go")
#plt.ylabel("loại điểm")
plt.xlabel('Số lượng')
plt.title('TRUNG BÌNH VAN')

plt.subplot(2,2,3)
plt.plot(df["Anh"], color = "blue") # , "go")
#plt.ylabel("loại điểm")
plt.xlabel('Số lượng')
plt.title('TRUNG BÌNH ANH')

plt.subplot(2,2,4)
plt.plot(df["XetTN"], color = "green") # , "go")
#plt.ylabel("loại điểm")
plt.xlabel('Số lượng')
plt.title('TRUNG BÌNH XETTN')

plt.suptitle("BIEU DO TOAN - VAN")
plt.show()