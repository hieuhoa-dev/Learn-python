from datetime import datetime
from SinhVien import SinhVien

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maso: int, hoTen: str, ngaySinh: datetime,trinhdo:str, tgdt: float) -> None:
        super().__init__(maso, hoTen, ngaySinh)
        self.trinhdo = trinhdo
        self.tgdt = tgdt

    def __str__(self) -> str:
        return super().__str__() + f"{self.trinhdo:<15} {self.tgdt:<15}"