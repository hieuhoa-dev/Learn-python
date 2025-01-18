from PhanSo import PhanSo
from DSPhanSo import DSPhanSo

tu= 2 
mau= 3 
a = PhanSo(tu,mau) 
b = PhanSo(3,5) 
print(f"Tổng: {a} + {b} = {a+b}") 
# 1/6 + 4/12 = 1/2 
print(f"Hiệu: {a} - {b} = {a-b}") 
print(f"Tích: {a} * {b} = {a*b}") 
print(f"Thương: {a} / {b} = {a/b}")

c= PhanSo(4,6)
ds = DSPhanSo()
ds.them(a)
ds.them(b)
ds.them(c)
print("Danh sách phân số: ")
ds.SapXep( tang = True,theoTu = True)
ds.xuat()
print("Phân số dương nhỏ nhất: ", ds.TimDuongNhoNhat())











