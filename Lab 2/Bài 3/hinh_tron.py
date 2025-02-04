from hinh_hoc import HinhHoc
from math import pi


class HinhTron(HinhHoc):
    def __init__(self, banKinh):
        super().__init__(banKinh)
        self._banKinh = banKinh 

    @property
    def BanKinh(self) -> float:
        return self._canh

    def TinhDienTich(self):
        return pi * self.BanKinh**2

    def Xuat(self) -> None:
        print(f"Hình Tròn - Bán kính: {self.BanKinh}, Diện tích: {self.TinhDienTich()}")

    def __str__(self):
        return f"Hình Tròn - Bán kính: {self.BanKinh}, Diện tích: {self.TinhDienTich()}"
