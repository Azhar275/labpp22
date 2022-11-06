lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

class BALOK :
    def __init__(self, lebar, tinggi, panjang) :
        self.wide= lebar
        self.height= tinggi
        self.long= panjang
    def setLebar(self, lebar) :
        self.wide= lebar
    def setTinggi(self, tinggi) :
        self.long= tinggi
    def setPanjang(self, panjang) :
        self.long= panjang
    def setMassa(self, massa) :
        self.weiht= massa
    def getMassaJenis(self) :
        return self.weiht/(self.long*self.wide*self.height)

kubus = BALOK(lebar, tinggi, panjang)
kubus.setLebar(24)
kubus.setTinggi(50)
kubus.setPanjang(98)
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setLebar(lebar)
print("Massa Jenis =", kubus.getMassaJenis())

