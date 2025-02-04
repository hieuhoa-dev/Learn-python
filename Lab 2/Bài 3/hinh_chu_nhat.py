from hinh_hoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai)
        # self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    @property
    def ChieuDai(self) -> float:
        return self._canh

    @property
    def ChieuRong(self) -> float:
        return self.chieu_rong

    def TinhDienTich(self):
        return self.ChieuDai * self.ChieuRong

    def Xuat(self) -> None:
        print(
            f"Hình Chữ Nhật - Dài: {self.ChieuDai}, Rộng: {self.ChieuRong}, Diện tích: {self.TinhDienTich()}"
        )

    def __str__(self):
        return f"Hình Chữ Nhật - Dài: {self.ChieuDai}, Rộng: {self.ChieuRong}, Diện tích: {self.TinhDienTich()}"
