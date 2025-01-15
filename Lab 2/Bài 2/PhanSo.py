from math import gcd

class PhanSo: 
    def __init__(self,tu,mau) -> None:
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.__tu = tu
        self.__mau = mau
        self.rutGon()

    
    def rutGon(self): 
        ucln = self.ucln(self.__tu, self.__mau) 
        # ucln = gcd(self.tu, self.mau)
        self.__tu //= ucln
        self.__mau //= ucln
        if self.mau < 0:  # Đưa dấu âm vào tử số
            self.tu = -self.tu
            self.mau = -self.mau

    
    def __add__(self, other): 
        tu = self.tu * other.mau + self.mau * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __sub__(self, other):
        tu = self.tu * other.mau - self.mau * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __mul__(self, other): 
        tu = self.tu * other.tu 
        mau = self.mau * other.mau
        return PhanSo(tu, mau) 

    def __truediv__(self, other): 
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số 0")
        tu = self.tu * other.mau 
        mau = self.mau * other.tu
        return PhanSo(tu, mau)  
    
    @property
    def tu(self): 
        return self.__tu
    @property
    def mau(self): 
        return self.__mau
    
    @tu.setter
    def tu(self, tu): 
        self.__tu = tu

    @mau.setter
    def mau(self, mau): 
        self.__mau = mau

    @staticmethod 
    def ucln(a,b): 
        while b!=0:
            a,b = b, a%b
        return a
    
    def __str__(self):
        return f"{self.tu}/{self.mau}" if self.mau != 1 else f"{self.tu}"
    

