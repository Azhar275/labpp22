class Person:
    def __init__(self, name, age, gender, makanan):
        self.name= name
        self.age= age
        self.gender= gender
        self.makanan= makanan
    
    def setName(self, name):
        self.name= name
    def getName(self):
        return self.name

    def setAge(self, age):
        self.age= age
    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender= gender
    def getGender(self):
        if self.gender == True:
            return 'Laki-laki'
        else:
            return 'Perempuan'  
        
    def setMakanan(self, makanan):
        self.makanan= makanan
    def getMakanan(self):
        return self.makanan
        
person1= Person('KELVIN', '18', True, 'Nasi goreng')
print(person1.getName())
print(person1.getAge())
print(person1.getGender())
print(person1.getMakanan())
person1.setName('Fail')
person1.setAge('20')
person1.setGender(False)
person1.setMakanan('Ayam bakar')
print(person1.getName())
print(person1.getAge())
print(person1.getGender())
print(person1.getMakanan())
print(person1.__dict__)