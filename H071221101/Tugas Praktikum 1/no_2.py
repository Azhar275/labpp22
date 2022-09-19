a = (input("masukkan detik : "))

jam = a // 3600
b = a % 3600
menit = b // 60
detik = b % 60

print("%02d:%02d:%02d"%(jam,menit,detik))