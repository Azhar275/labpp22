jumlah_detik= int (input("Mohon Masukkan Jumlah Detik : "))

jam=jumlah_detik//3600
sisa_detik=jumlah_detik-3600*jam
menit=sisa_detik//60
detik=sisa_detik-(60*menit)

print("%d : %02d : %d "%(jam, menit, detik))