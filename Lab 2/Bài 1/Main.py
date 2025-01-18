
from datetime import datetime
from DanhSachSv import DanhSachSv
from SinhVien import SinhVien

# Tạo danh sách sinh viên
dssv = DanhSachSv()
fileName = "D:\Learn Python\Lab 2\Bài 1\sinhvien.txt"
dssv.doc_file_sinh_vien(fileName)
dssv.xuat()
