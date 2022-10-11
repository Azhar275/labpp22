# Soal Modul
n = int(input("Jumlah angka : "))
a = 0 ; b = 1 ; c = a + b
for i in range(n):
    print(a, end=" ")
    a = b ; b = c ; c = a + b
    
# Soal Prak
while True:
    derajat = (input("Masukkan derajat :")) 
    c = ''
    if derajat is not c:
        waktu = (1 / 15) * 3600 * float(derajat)
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
    else:
        break
