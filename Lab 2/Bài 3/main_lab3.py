from ds_hinh_hoc import DanhSachHinhHoc
from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh

# Chạy thử chương trình
ds = DanhSachHinhHoc()
ds.themHinh(HinhTron(3))
ds.themHinh(HinhVuong(4))
ds.themHinh(HinhChuNhat(5, 6))


print("Danh sách hình học:")
print(ds)

print("\nHình có diện tích lớn nhất:")
# print(ds.timHinhCoDienTichLonNhat())
print("\n".join(str(h) for h in ds.timHinhCoDienTichLonNhat()))

print("\nHình có diện tích nhỏ nhất:")
print(ds.timHinhCoDienTichNhoNhat())

# print("\nHình tròn có diện tích nhỏ nhất:")
# print(ds.TimHinhTronNhoNhat())

print("\nSố hình tròn trong danh sách:")
print(ds.DemSoLuongHinh(LoaiHinh.HinhTron))

print("\nSố hình tròn trong danh sách:")
print(ds.DemSoLuongHinh(LoaiHinh.TatCa))

print("\nSắp xếp giảm dần theo diện tích:")
ds.SapGiamTheoDienTich()

print("\nDanh sách hình học sau khi sắp xếp:")
print(ds)

print("\nTìm hình có diện tich lớn nhất của hình vuong:")
print(ds.TimHinhCoDienTichLonNhat(LoaiHinh.HinhVuong))
