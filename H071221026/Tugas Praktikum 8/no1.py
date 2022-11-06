class person :
    def __init__(self, nama, umur, gender, hobi) :
        self.name= nama
        self.age= umur
        self.isMale= gender
        self.hobbies= hobi

    def setAge(self, umur) :
        self.age= umur
    def getAge(self) :
        print(f"Umur : {self.age}")

    def setName(self, nama) :
        self.name= nama
    def getName(self) :
        print(f"Nama : {self.name}")

    def setGender(self, gender) :
        self.isMale= gender
    def getGender(self) :
        if self.isMale== True :
            print("gendernya laki-laki")
        else :
            self.isMale== False
            print("gendernya bukan laki-laki")

    def setHobi(self, hobi) :
        self.hobbies= hobi
    def getHobi(self) :
        print(f"Hobi {self.name} asalah : {self.hobbies}")

alex= person("alex", 22, True, "Belajar")
alex.getName()
alex.getAge()
alex.getGender()
alex.getHobi()