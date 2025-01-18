from datetime import datetime
from SinhVien import SinhVien
from sv_CQ import SinhVienChinhQuy
from sv_phi_CQ import SinhVienPhiCQ
class DanhSachSv: 
    header = ["ID", "Họ và tên", "Ngày sinh", "Bằng cấp", "Điểm"]

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

    def timSvTheoLoai (self, loai: str): 
        if loai == "chinhquy":
             return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)] 
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
    

    def doc_file_sinh_vien(self,file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = [x.strip() for x in line.split(",")]
                mssv = int(data[0])  # Xác định loại sinh viên
                ho_ten = data[1]
                ngay_sinh = datetime.strptime(data[2], "%d/%m/%Y")

                if len(data)==4:
                    diem_ren_luyen = float(data[3])  
                    sv = SinhVienChinhQuy(mssv,ho_ten, ngay_sinh, diem_ren_luyen)
                elif len(data)==5:
                    trinhdo = data[3] 
                    tgdt = float(data[4])
                    sv = SinhVienPhiCQ(mssv,ho_ten, ngay_sinh, trinhdo,tgdt)
                else:
                    print(f"Dòng dữ liệu không hợp lệ: {line}")
                    continue
                self.themSinhVien(sv)
        