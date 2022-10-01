derajat = float(input("Masukkan derajat :"))
waktu = (1 / 15) * 3600 * derajat
print(waktu)
jam = waktu // 3600
C = waktu % 3600
Menit = C // 60
detik = C % 60 
o = (jam + 6) % 24
if o >= 0 and o <= 11:
    print("Selamat Pagi!")
elif o > 11 and o <= 15:
    print("Selamat siang!")
elif o > 15 and o <= 18:
    print("Selamat sore!")
elif o > 18 and o <= 24:
    print("Selamat Malam!")
print("%02d:%02d:%02d" % ((o, Menit, detik)))