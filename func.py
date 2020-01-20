def tong(a,b):
    return a+b

a = int(input("Nhap so thu 1: "))
b = int(input("Nhap so thu 2: "))
c = tong(a,b)
print(c)

def chao(ten):
    """De giai thich cho ham"""
    print("Xin chao, ", ten)

chao("Quantrimang")
print(chao.__doc__)
