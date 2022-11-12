class Bio:

    def __init__(self, name, age, isMale):
        self.name=name
        self.age=age
        self.isMale=isMale

    def setName(self, name):
        self.name=name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age=age

    def getAge(self):
        return self.age

    def setGender(self):
        self.isMale=isMale

    def getGender(self):
        if self.isMale==True:
            return 'Laki-Laki'
        else:
            return 'Perempuan'

name=input('name: ')
age=int(input('age: '))
isMale=bool(input('isMale: '))

bio=Bio(name, age, isMale)

bio.setName(bio.getName())
print(bio.getName())

bio.setAge(bio.getAge())
print(bio.getAge())

bio.setGender()
print(bio.getGender())
