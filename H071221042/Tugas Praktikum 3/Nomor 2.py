derajat= float(input())

waktu= (1/15)*3600*derajat
jam= waktu//3600
sisa_detik=waktu-3600*jam
menit=sisa_detik//60
detik=sisa_detik-(60*menit)
jam+=6
    
if jam >0 and jam <12:
    print('Selamat Pagi')
elif jam >=12 and jam <=15:
    print('Selamat Siang')
elif jam >15 and jam <=18:
    print('Selamat Sore') 
elif jam >18 and jam <=24:
    print('Selamat Malam')
elif jam >0:
    print('Selamat Pagi')
print("%02d:%02d:%02d"%(jam%24, menit, detik))
   
try:
    while True:
        derajat= float(input())
    
        waktu= (1/15)*3600*derajat    
        jam= waktu//3600
        sisa_detik=waktu-3600*jam
        menit=sisa_detik//60
        detik=sisa_detik-(60*menit)
        jam+=6

        if jam >0 and jam <12:
            print('Selamat Pagi')
        elif jam >=12 and jam <=15:
            print('Selamat Siang')
        elif jam >15 and jam <=18:
            print('Selamat Sore') 
        elif jam >18 and jam <=24:
            print('Selamat Malam')
        elif jam >0:
            print('Selamat Pagi')
            
        print("%02d:%02d:%02d"%(jam%24, menit, detik))
except:
    print("Inputan salah\nMohon coba lagi dan masukkan angka")
    