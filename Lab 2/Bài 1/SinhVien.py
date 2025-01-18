from datetime import datetime

class SinhVien: 
    truong = "Đại học Đà Lạt"  
    def __init__(self, maso: int, hoTen: str, ngaySinh: datetime) -> None: 
        self._maso = maso 
        self._hoTen = hoTen 
        self._ngaySinh = ngaySinh
       
    
    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maso
    @property 
    def maso(self): 
        return self._maso 
    
    def hoTen(self): 
        return self._hoTen 
        
    def ngaySinh(self): 
        return self._ngaySinh 
        
    # cho phép thay đổi giá trị thuộc tính maso
    @maso.setter 
    def maso(self, maso): 
        if self.laMaSoHopLe(maso):
            self._maso = maso
    
    # phương thức tình: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp 
    # những phương thức này không cần truyền tham số mặc định self 
    # đây không phải là một hành vi (phương thức) của 1 đối tượng thuộc lớp 
    @staticmethod 
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    # phương thức của lớp, chỉ truy xuất tới các biến thành viên của lớp 
    # không truy xuất được các thuộc tính riêng của đối tượng 
    @classmethod 
    def doiTenTruong (self, tenmoi): 
        self.truong = tenmoi 
    
    def __str__(self) -> str: 
        ngaySinh_str = self._ngaySinh.strftime("%d-%m-%Y") if hasattr(self._ngaySinh, "strftime") else self._ngaySinh
        return f"{self._maso:<10} {self._hoTen:<20} {ngaySinh_str:<15}" 
    
    # hành vi của đối tượng sinh viên 
    def xuat(self): 
        print(f"{self._maso:<10} {self._hoTen:<20} {self._ngaySinh:<15}")