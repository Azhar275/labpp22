import re
class Data:
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Nama
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    # Email dan validasinya
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email

    # Password dan validasinya
    def setPass(self, password):
        self.password = password
    def getPass(self):
        return self.password

    def save(self, filename):
        try:
            with open(filename+'.txt','r') as file:
                file.read()
            with open(filename+'.txt','a') as file:
                file.write('Name'.ljust(10)+':'+self.name+'\n')
                file.write('Email'.ljust(10)+':'+self.email+'\n')
                file.write('Password'.ljust(10)+':'+self.password+'\n')
                file.write(50*'='+'\n')
        except:
            with open(filename+'.txt','a') as file:
                file.write(50*'='+'\n')
                file.write('Data yang Tersimpan'.center(50)+'\n')
                file.write(50*'='+'\n')
                file.write('Name'.ljust(10)+':'+self.name+'\n')
                file.write('Email'.ljust(10)+':'+self.email+'\n')
                file.write('Password'.ljust(10)+':'+self.password+'\n')
                file.write(50*'='+'\n')

    def count(filename):
        with open(filename+'.txt') as file:
            return ((len(file.readlines())//3)-1)