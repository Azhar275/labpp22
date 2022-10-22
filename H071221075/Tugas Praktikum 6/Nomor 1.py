a, b = input("File Asli : ")+'.txt', input("File salinan : ")+'.txt'
try:
    def salin(a, b):
        with open(a) as asli:
            file_as = asli.read()
            with open(b, "w") as salinan:
                salinan.write(file_as) ; print("Berhasil")
    salin(a,b)
except FileNotFoundError: 
    print("Gagal")
