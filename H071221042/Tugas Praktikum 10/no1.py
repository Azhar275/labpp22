import re
import os
def bikindata ():
    data = {
        "Nama" : input("Masukkan nama: "),
        "email" : "",
        "password" : ""
    }
    cekemail= 0
    while cekemail== 0:
        data ["email"]= input("Masukkan email: ")
        cekEmail = "^[a-z0-9]{1,}@student.unhas.ac.id$"
        if re.search(cekEmail, data["email"]):
            cekemail= 1
        else:
            print("=" * 60)
            print("Format email salah\nSilahkan masukkan email lagi!")
            print("=" * 60)
    cekpassword= 0
    while cekpassword == 0:
        data ["password"]= input("Masukkan password: ")
        cekpass= "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$"
        if len(data["password"]) >= 8:
            if re.search(cekpass, data["password"]):
                cekpassword= 1
            else:
                print("=" * 60)
                print("Password Terlalu Lemah")
                print("Harus Memiliki Minimal 1 Huruf Kapital, Huruf Kecil, dan juga Angka")
                print("=" * 60)
        else:
            print("=" * 60)
            print("Panjang Password harus 8-20 Karakter")
            print("=" * 60)
    return data

def jumlahdata():
    namafile= input("Masukkan Nama File: ")
    x= "@student.unhas.ac.id"
    try:
        with open(f"{namafile}.txt", "r") as item:
            jumlah= re.findall(x, item.read())
        print("Berhasil")
        print(f"Jumlah data di File: {jumlah.count(x)} Data")
    except FileNotFoundError:
        print(f"Tidak Ada File dengan Nama {namafile}.txt")
        print("Jumlah Data Pada File: 0")

def savedata():
    file = input("Input Nama File: ")
    if os.path.exists("{file}.txt"):
        item.write("+" + "="*50 + "\n")
        item.write("|Data yang Tersimpan\n")
        item.write("+" + "="*50 + "\n")
        with open(f"{file}.txt", "w") as item:
            for x, value in data.items():
                item.write(f"|{x} : {value}\n")

    else:
        with open(f"{file}.txt", "a") as item2:
            for z, value in data.items():
                item2.write(f"|{z} : {value}\n")
    print("Berhasil")



data= None
while True:
    print("="*60)
    print("Selamat Datang\nSilahkan Pilih Opsi Di Menu Anda")
    print("1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data pada File\n4. Save Data pada File\n5. Buat Data Baru\n6. Keluar")
    x= int(input("Pilih Opsi: "))
    print("="*60)
    match x:
        case 1:
            if data == None:
                print("Data saat ini kosong")
            else:
                print("Data Anda adalah")
                for key, value in data.items():
                    print(f"{key} : {value}")
        case 2:
            if data == None:
                print("Data saat ini kosong")
            else:
                data["Nama"] = input("Masukkan Nama Baru: ")
                print("Berhasil")
        case 3:
            jumlahdata()
        case 4:
            if data== None:
                print("Data saat ini kosong")
            else:
                savedata()
        case 5:
            data= bikindata()
        case 6:
            print("Terima Kasih Telah Menggunakan Program")
            print("=" * 50)
            break