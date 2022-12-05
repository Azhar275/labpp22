from abc import ABC, abstractclassmethod

class MahklukHidup(ABC):

    @abstractclassmethod
    def setGender(self):
        pass
    def getGender(self):
        pass

class Hewan(MahklukHidup):
    def __init__(self, nama, gender):
        self.__nama=  nama
        self._gender= gender
    
    def setNama(self, nama):
        self.nama= nama
    def getNama(self):
        return self.nama

    def setGender(self, gender):
        self.gender= gender
    def getGender(self):
        if self.gender == True:
            return 'Jantan'
        else:
            return 'Betina'  

class Unggas(Hewan):
    def __init__(self, nama, gender):
        super().__init__(nama, gender)

    
    def Bergerak(self):
        print("Unggas Bergerak dengan Cara Terbang")

class Amfibi(Hewan):
    def __init__(self, nama, gender):
        super().__init__(nama, gender)
    
    def Bergerak(self):
        print("Amfibi Bergerak Dengan Cara Berenang")


ayam= Unggas("Ayam", True)
ayam.Bergerak()

kodok= Amfibi("Kodok", True)
kodok.Bergerak()
print(ayam.__dict__)