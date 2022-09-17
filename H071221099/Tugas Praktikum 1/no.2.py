detik = int(input("masukkan detik : "))
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik_real = sisa_detik % 60

if menit > 10 :
    print("%d:0%d:%d" % (jam,menit,detik_real))
else :
    print("%d:0%d:%d" % (jam,menit,detik_real))
