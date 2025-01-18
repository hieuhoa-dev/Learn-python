from datetime import datetime
from SinhVien import SinhVien

class SinhVienChinhQuy(SinhVien):
    def __init__(self, maso: int, hoTen: str, ngaySinh: datetime, diemRL: float) -> None:
        super().__init__(maso, hoTen, ngaySinh)
        self.diemRL = diemRL

    def __str__(self) -> str:
        return super().__str__() + f"{self.diemRL:<15}"