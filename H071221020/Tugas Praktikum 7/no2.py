
import re
x = int(input()) #input jumlah baris
ipl = [] #list kosong umtuk diisi hasil input
for i in range(0,x): #perulangan jumlah baris inputan
    ip = input() #inpiutan ip
    ipl.append(ip) #memasukkan input ke ipl
for j in ipl: #perulangan untuk pengecekan
    i4=False
    i6=False
    if re.match('^((\d|[a-f]){1,4}:){7}(\d|[a-f]){1,4}$',j):
        i6=True
    else:
        i4 = re.match('^((((\d){1,3})(\.)){3})((\d){1,3})$',j)
        cek=j.split('.') #dipisah untuk pengecekan jumlah di i4
        jum=[] #list kosong untuk menyimpan elemen yang dipisah dalam tipe int
        try: #untuk menangani eror apabila inputan bukan angka
            for k in cek:
                k=int(k)
                jum.append(k)
            if max(jum)<=255 and i4: #memerikasa jumlah dan kecocokan i4
                i4=True
            else:
                i4=False
        except ValueError:
            i4=False
    if i4:
        print('IPv4')
    elif i6:
        print('IPv6')
    else:
        print('Bukan IP Address')