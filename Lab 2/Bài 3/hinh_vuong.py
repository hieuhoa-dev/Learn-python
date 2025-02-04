from hinh_chu_nhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh, canh)

    def Xuat(self) -> None:
        print(f"Hình Vuông - Cạnh: {self._canh}, Diện tích: {self.TinhDienTich()}")

    def __str__(self):
        return f"Hình Vuông - Cạnh: {self._canh}, Diện tích: {self.TinhDienTich()}"
