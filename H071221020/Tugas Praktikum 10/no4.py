from abc import ABC, abstractmethod

class Abs(ABC):
    @abstractmethod
    def getName():
        pass

class Person():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def getName(self):
        return self.name

class Tkgpukul(Person):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.kekuatan = 50
    def Menyekiti(self, target):
        target.power-=self.kekuatan
    def MintaTolong(self):
        self.power+=30
    def getPower(self):
        return self.power

class Tkgtendang(Person):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.kekuatan = 75
    def Menyekiti(self, target):
        target.power-=self.kekuatan
    def MintaTolong(self):
        self.power+=15
    def getPower(self):
        return self.power

op1 = int(input('Masukkan pilihan pemain 1: '))
if op1==1:
    name_1 = input('Masukkan nama: ')
    player_1 = Tkgpukul(name_1, 500)
elif op1==2:
    name_1 = input('Masukkan nama: ')
    player_1 = Tkgtendang(name_1, 350)

op2 = int(input('Masukkan pilihan pemain 2: '))
if op1==1:
    name_2 = input('Masukkan nama: ')
    player_2 = Tkgpukul(name_2, 500)
elif op1==2:
    name_2 = input('Masukkan nama: ')
    player_2 = Tkgtendang(name_2, 350)

print(50*'=')
print('WAKTUNYA BERMAIN'.center(50))
print(50*'=')

while True:
    p1 = int(input(f'apa yang akan dilakukan {name_1}? '))
    if p1==1:
        player_1.Menyekiti(player_2)
        print(f'sisa power {name_2}: {player_2.getPower()}')
    elif p1==2:
        player_1.MintaTolong()
        print(f'power {name_1} menjadi: {player_1.getPower()}')

    p2 = int(input(f'apa yang akan dilakukan {name_2}? '))
    if 2==1:
        player_2.Menyekiti(player_1)
        print(f'sisa power {name_1}: {player_1.getPower()}')
    elif p2==2:
        player_2.MintaTolong()
        print(f'power {name_2} menjadi: {player_2.getPower()}')
    maulagi = int(input('mau lagi? '))
    if maulagi==0:
        break