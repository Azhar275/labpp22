lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

class kubus :
    def __init__(self, lebar, tinggi, panjang) :
        self.lebar= lebar
        self.tinggi= tinggi
        self.panjang= panjang
    def setLebar(self, lebar) :
        self.lebar= lebar
    def setTinggi(self, tinggi) :
        self.tinggi= tinggi
    def setPanjang(self, panjang) :
        self.panjnag= panjang
    def setMassa(self, massa) :
        self.massa= massa
    def getMassaJenis(self) :
        return self.massa/(self.panjang*self.lebar*self.tinggi)

kubus = kubus (lebar, tinggi, panjang)
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())