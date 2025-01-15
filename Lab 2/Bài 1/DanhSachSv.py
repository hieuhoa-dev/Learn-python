from datetime import datetime
from SinhVien import SinhVien

class DanhSachSv: 
    def __init__(self) -> None: 
        self.dssv = [] 

    def themSinhVien(self, sv: SinhVien):
         self.dssv.append(sv) 

    def xuat(self):
         for sv in self.dssv: 
             print(sv)

    # tìm sinh viên theo mssv, nếu có trả về sinh viên
    def timSvTheoMssv(self, mssv: int): 
        return [ sv for sv in self.dssv if sv.mssv == mssv] 
    
    # tìm sinh viên theo mssv, nếu có trả về vị trí của sinh viên trong danh sách 
    def timVTSvTheoMssv (self, mssv: int): 
        for i in range(len(self.dssv)): 
            if self.dssv[i].mssv == mssv:
                return i
            return -1

    # xóa sinh viên có mã số mssv, thông báo xóa dc hoặc ko 
    def xoaSvTheoMssv (self, maso: int) -> bool:
        vt = self.timVTSvTheoMssv(maso)
        if vt != -1: 
            del self.dssv[vt] 
            return True 
        else: 
            return False 
        
    # tìm sinh viên tên "Nam" 
    def timSvTheoTen(self, ten: str): 
         return [ sv for sv in self.dssv if sv.hoTen.contains(ten)]  
    
    # tìm những sinh viên sinh trước 15/6/2000 
    def timSvSinhTruocNgay (self, ngay: datetime): 
         return [ sv for sv in self.dssv if sv.ngaySinh < ngay]
    
    def sapXepTheoTen(self): 
        self.dssv.sort(key=lambda sv: sv.hoTen)
