class Elektronik:
    def __init__(self, merk) -> None:
        self.harga = 0
        self.merk = merk

    def setHarga(self, harga):
        self.harga = harga
    
    def getHarga(self):
        return self.harga

    def nyalakan(self):
        print(f"{self.merk} Menyela")

class Handphone(Elektronik):
    def __init__(self, merk, harga):
        super().__init__(merk)
        self.harga = harga
        self.baterai = 5

    def charge(self):
        self.baterai = 100

    def layar(self):
        print(f"{self.merk} Layarnya Kecil")


class Laptop(Elektronik):
    def __init__(self, merk, harga):
        super().__init__(merk)
        self.harga = harga
        self.baterai = 10

    def layar(self):
        print(f"{self.merk} Layarnya Besar")
    

HP = Handphone("Samsung", 5000)
laptop = Laptop("Asus", 20000)

HP.layar()
laptop.layar()