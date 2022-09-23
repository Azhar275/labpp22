x = int(input("Masukkan detik : "))
jam = x / 3600
C = x % 3600
Menit = C / 60
detik = C % 60
print("%d jam, %02d menit, %02d detik." % (jam, Menit, detik))
print("%02d:%02d:%02d" % (jam, Menit, detik))


