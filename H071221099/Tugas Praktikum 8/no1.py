class Person:
    def __init__(self, name, age, matkul, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.matkul = matkul 

    def setAge (self, age):
        self.age = int(age)

    def getAge (self):
        return self.age

    def setName (self, name):
        self.name = name 

    def getName (self):
        return self.name

    def setMatkul (self, matkul):
        self.matkul = matkul

    def getMatkul (self):
        return self.matkul
        
    def setGender (self, gender):
        if gender ==  "male":
            self.isMale = True
        else:
            self.isMale = False 

    def getGender (self):
        if self.isMale == True:
            self.gender = "male"
            return self.gender
        else:
            self.gender = "female"
            return self.gender

name = input ("masukkan nama: " )
Age = int(input ("masukkan umur: "))
matkul = input("masukkan matkul:")
isMale = input ("ismale? True or False: ").upper()
if isMale == "TRUE":
    isMale = bool(True)
else:
    isMale = bool(False)

person = Person(name, Age, matkul, isMale)
print(person.getName())
print(person.getAge())
print(person.getGender())
print(person.getMatkul())

