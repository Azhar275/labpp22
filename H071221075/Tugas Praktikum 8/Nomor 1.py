class human:
    def __init__(self, name, age, isMale, tinggi):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self.tinggi
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
    def setGender(self, isMale):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return("Male")
        elif self.isMale == False:
            return("Female")
Rio = human("Rio", 19, True, 171)
Kelvin = human("kelvin",20,False,140)
print(Rio.getGender())
print(Kelvin.getGender())
