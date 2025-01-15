
from datetime import datetime
from DanhSachSv import DanhSachSv
from SinhVien import SinhVien

# Tạo danh sách sinh viên
dssv = DanhSachSv()
fileDSSV = open("sinhvien.txt", "r", encoding="utf-8")
for line in fileDSSV:
     try:
        s = [x.strip() for x in line.split(",")]
        # mssv = int(s[0])
        # hoTen = s[1]
        # ngaySinh = datetime.strptime(s[2], "%d/%m/%Y")
        # sv = SinhVien(mssv, hoTen, ngaySinh)
        # dssv.themSinhVien(sv)
        dssv.themSinhVien(SinhVien(int(s[0]), s[1], datetime.strptime(s[2], "%d/%m/%Y")))
     except ValueError:
        print(f"Dữ liệu không hợp lệ: {line}")

dssv.xuat()