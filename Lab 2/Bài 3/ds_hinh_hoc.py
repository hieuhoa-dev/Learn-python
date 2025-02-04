from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh


class DanhSachHinhHoc:
    def __init__(self):
        self.ds_hinh = []

    def themHinh(self, hinh):
        self.ds_hinh.append(hinh)

    def xuat(self):
        for hinh in self.ds_hinh:
            print(hinh)

    def __str__(self) -> str:
        return "\n".join(str(hinh) for hinh in self.ds_hinh)

    def timHinhCoDienTichLonNhat(self):
        if not self.ds_hinh:  # Nếu danh sách rỗng, trả về danh sách rỗng
            return []
        max_dien_tich = max(h.TinhDienTich() for h in self.ds_hinh)
        return [h for h in self.ds_hinh if h.TinhDienTich() == max_dien_tich]

    def timHinhCoDienTichNhoNhat(self) -> "DanhSachHinhHoc":
        ds_min = DanhSachHinhHoc()
        if not self.ds_hinh:  # Nếu danh sách rỗng, trả về danh sách rỗng
            return ds_min
        min_dien_tich = min(h.TinhDienTich() for h in self.ds_hinh)
        for h in self.ds_hinh:
            if h.TinhDienTich() == min_dien_tich:
                ds_min.themHinh(h)
        return ds_min

    def TimHinhTronNhoNhat(self):
        if not self.ds_hinh:
            return []
        min_dien_tich = min(
            h.TinhDienTich() for h in self.ds_hinh if isinstance(h, HinhTron)
        )
        return [h for h in self.ds_hinh if h.TinhDienTich() == min_dien_tich]

    def TimHinhTheoDTich(self, dt: float):
        return [h for h in self.ds_hinh if h.TinhDienTich() == dt]

    def SapGiamTheoDienTich(self) -> None:
        self.ds_hinh.sort(key=lambda h: h.TinhDienTich(), reverse=True)

    def DemSoLuongHinh(self, kieu: LoaiHinh):
        if kieu == LoaiHinh.TatCa:
            return len(self.ds_hinh)

        loai_hinh_map = {
            LoaiHinh.HinhTron: HinhTron,
            LoaiHinh.HinhChuNhat: HinhChuNhat,
            LoaiHinh.HinhVuong: HinhVuong,
        }
        if kieu not in loai_hinh_map:
            return 0  # Nếu loại hình không hợp lệ thì trả về 0

        return len([h for h in self.ds_hinh if isinstance(h, loai_hinh_map[kieu])])

    def TinhTongDienTich(self) -> float:
        return sum(h.TinhDienTich() for h in self.ds_hinh)

    def TimHinhCoDienTichLonNhat(self, kieu: LoaiHinh) -> "DanhSachHinhHoc":
        ds_max = DanhSachHinhHoc()
        if not self.ds_hinh:
            return ds_max
        loai_hinh_map = {
            LoaiHinh.HinhTron: HinhTron,
            LoaiHinh.HinhChuNhat: HinhChuNhat,
            LoaiHinh.HinhVuong: HinhVuong,
        }
        # Tìm diện tích lớn nhất của loại hình
        max_dien_tich = max(
            h.TinhDienTich() for h in self.ds_hinh if isinstance(h, loai_hinh_map[kieu])
        )
        # Tìm danh sach hình có diện tích lớn nhất
        for h in self.ds_hinh:
            if h.TinhDienTich() == max_dien_tich:
                ds_max.themHinh(h)
        return ds_max
