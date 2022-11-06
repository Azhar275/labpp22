class Bio:

    def __init__(self, name, age, isMale):
        self.name=name
        self.age=age
        self.isMale=isMale
        if int(self.isMale)==0:
            self.isMale=bool('')

    def setName(self, name):
        self.name=name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age=age

    def getAge(self):
        return self.age

    def getisMale(self):
        return self.isMale

    def setGender(self, isMale):
        self.isMale=isMale

    def getGender(self):
        if bio.getisMale()==True:
            return 'Laki-Laki'
        else:
            return 'Perempuan'

while True:
    name=input('name: ')
    age=int(input('age: '))
    isMale=bool(input('isMale: '))

    bio=Bio(name, age, isMale)

    bio.setName(bio.getName())
    print(bio.getName())

    bio.setAge(bio.getAge())
    print(bio.getAge())

    bio.setGender(bio.getisMale())
    print(bio.getGender())

    x = int(input())
    if x==0:
        break