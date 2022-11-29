from Data import Data
import re

while True:
    print('Selamat Datang Silakan Pilih Opsi Menu Anda')
    print(' 1. Detail Anda')
    print(' 2. Ubah Nama')
    print(' 3. Jumlah Data pada File')
    print(' 4. Save Data pada File')
    print(' 5. Buat Data Baru')
    print(' 6. Keluar')
    op = int(input('Silakan Pilih Opsi Menu Anda '))
    if op==1:
        try:
            print(data.getName())
            print(data.getEmail())
            print(data.getPass())
        except:
            print('Data saat ini kosong')
    elif op==2:
        try:
            data.getName()
            name = input()
            data.setName(name)
        except:
            print('Data saat ini kosong')
    elif op==3:
        try:
            filename = input()
            print(Data.count(filename))
        except:
            print('Tidak Terdapat File dengan Nama {}.txt'.format(filename))
    elif op==4:
        try:
            filename = input()
            data.save(filename)
            print('Berhasil')
            delattr(data, 'name')
            delattr(data, 'email')
            delattr(data, 'password')
        except:
            print('Data saat ini kosong')
    elif op==5:
        name = input()
        email = 'True'
        password = 'True'
        while bool(re.match('^[a-z0-9]+\@student\.unhas\.ac\.id$', email))==False:
            email = input()
            if bool(re.match('^[a-z0-9]+\@student\.unhas\.ac\.id$', email))==False:
                print('Email yang Anda Masukkan Salah')
        while bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', password))==False:
            password = input()
            if bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', password))==False:
                print('Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka')
        data = Data(name, email, password)
    elif op==6:
        print('SAMPAI JUMPA LAGI')
        break
