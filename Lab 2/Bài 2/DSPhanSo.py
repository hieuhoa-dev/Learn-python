from PhanSo import PhanSo 

class DSPhanSo:
    def __init__(self) -> None:
        self.__ds = []
    
    def them(self, ps: PhanSo):
        self.__ds.append(ps)

    def xuat(self):
        for ps in self.__ds:
            print(ps)

    #Đếm số phân số âm trong mảng   
    def DemSoAm(self):
        return len([ps for ps in self.__ds if ps.tu < 0])   
    
    # Tìm phân số dương nhỏ nhất
    def TimDuongNhoNhat(self):
        dsDuong = [ps for ps in self.__ds if ps.tu > 0]
        if len(dsDuong) == 0:
            return None
        return min(dsDuong, key=lambda ps: ps.tu/ps.mau)
    
    # Tổng tất cả các phân số âm trong mảng
    def TongAm(self):
        return sum([ps for ps in self.__ds if ps.tu < 0])
    
    # Xóa phân số x trong mảng
    def Xoa(self, x: PhanSo):
        self.__ds.remove(x)

    # Xóa tất cả phân số có tử là x
    def XoaTatCa(self, x: int):
        self.__ds = [ps for ps in self.__ds if ps.tu != x]

    # Sắp xếp phân số theo chiều tăng, giảm; tăng theo mẫu, tử, giảm theo mẫu tử
    def SapXep(self, tang: bool, theoTu: bool):
        self.__ds.sort(key=lambda ps: ps.tu if theoTu else ps.mau, reverse=not tang)


    

