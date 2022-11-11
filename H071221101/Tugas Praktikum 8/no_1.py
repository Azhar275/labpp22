# creat class
class person:

    def __init__(self, name, age, gender, alamat):
        self.name = name
        self.age = age
        self.gender = gender
        self.alamat = alamat
    
    def setAge(self, age) :
        self.age = age
    def getAge(self):
        return self.age
    def setName(self, name) :
        self.name = name
    def getName(self):
        return self.name
    def setGender(self, gender) :
        self.gender = gender
    def getGender(self):
        if self.gender == True :
            return "Male"
        else :
            return "Female"
    def setAlamat(self, alamat) :
        self.alamat = alamat
    def getAlamat (self) :
        return self.alamat

data = person("el", 18, False, "Isekai")
print(data.getAge())
print(data.getName())
print(data.getGender())
print(data.getAlamat())
data.setName("lisa")
print(data.getName())