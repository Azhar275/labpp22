import math
h = int (input("Masukkan Ketinggian Menara (dalam satuan meter):"))
a = float (input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap U:"))
b = float (input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap U:"))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan 

print ("Panjang kapalnya adalah %5.2f m" % (panjang) )