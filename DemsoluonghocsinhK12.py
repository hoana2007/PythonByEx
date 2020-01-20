import pandas as pd
from pandas import ExcelFile

hs_path = 'H:\Python\PythonApplication1\k12.xlsx'
df = pd.read_excel(hs_path)

#Lay dau, cuoi
#print(df.head(5))
#print(df.tail(5))

#Xem thong tin trong Dataframe
print("thong tin Fame: ", df.info())

#Chieu dai cua Frame
print("Thong tin chieu dai Frame: ", len(df))

#Kich thuoc Frame
print("Kich thuoc Frame: ", df.shape)

#Lay du lieu theo cot
print(df[["Hoten","Toan", "TBToan"]])

#Lay day cot
print(df[0:3])

#Lay du lieu cot hang ket hop
print(df[["Hoten","TBToan"]][:5])

#Lay ban ghi theo dieu kien
#Lop
lop = df[df["Lop"] == "12A"]
print(lop[:4])

#Thong ke co ban
print(df.describe())

#Sap xep
print(df.sort_values(["XetTN"], ascending = False))


