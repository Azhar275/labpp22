import re

name = []
email = []
password = []

while True:
    print(50*'=')
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah data pada file")
    print("4. Save data pada file")
    print("5. Buat data Baru")
    print("6. Keluar")
    opsi = int(input("silahkan pilih opsi anda : "))

    if opsi == 1:
        if len(name) == 0 or len(email) == 0 or len(password) == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            print("Data anda adalah")
            for nama in name:
                print(f"Nama : {nama}")
            for mail in email:
                print(f"Email : {mail}")
            for pas in name:
                print(f"Password : {pas}")
    elif opsi == 2:
        if len(name) == 0 or len(email) == 0 or len(password) == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            newName = input("Silahkan input nama baru : ")
            name[0] = newName
    elif opsi == 3:
        print(50*'=')
        fileName = input("Silahkan masukkan nama file : ")
        try:
            with open(f"{fileName}.txt") as file:
                data = file.read()
                total = data.count("@student.unhas.ac.id")
                print(f"Jumlah data anda adalah : {total} data")
        except:
            print(f"tidak terdapat file dengan nama {fileName}.txt")
            print(f"Jumlah data anda adalah : 0 data")
    elif opsi == 4:
        if len(name) == 0 or len(email) == 0 or len(password) == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            namafile = input("Masukkan Nama file baru anda : ")
            try:
                for k in range(len(name)):
                    with open(f"{namafile}.txt") as baca:
                        baca.read()
                    with open(f"{namafile}.txt", "a") as table:
                        table.write(f"|Nama     : {name[k]}\n")
                        table.write(f"|Email    : {email[k]}\n")
                        table.write(f"|Password : {password[k]}\n")
                        table.write(f"+{'='*70}\n")
            except:
                for k in range(len(name)):
                    with open(f"{namafile}.txt", "a") as table:
                        table.write(f"+{'='*70}\n")
                        table.write(f"|Data yang tersimpan\n")
                        table.write(f"+{'='*70}\n")
                        table.write(f"|Nama     : {name[k]}\n")
                        table.write(f"|Email    : {email[k]}\n")
                        table.write(f"|Password : {password[k]}\n")
                        table.write(f"+{'='*70}\n")
            name.clear()
            email.clear()
            password.clear()
            print("Berhasil")
    elif opsi == 5:
        print(50*'=')
        namaku = input("Silahkan masukkan nama anda : ")
        name.append(namaku)
        while True:
            emailku = input("Silahkan masukkan email anda : ")
            if re.match("^[a-z0-9]+\@student\.unhas\.ac\.id$", emailku):
                email.append(emailku)
                break
            else:
                print(50*'=')
                print("Email yang anda masukkan salah")
                print(50*'=')

        while True:
            passwordku = input('Silahkan masukkan password anda : ')
            if re.match("[\dA-Za-z]{8,20}", passwordku):
                if re.match("[\dA-Za-z]", passwordku):
                    password.append(passwordku)
                    break
                else:
                    print(50*'=')
                    print(
                        "Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
                    print(50*'=')
            else:
                print(50*'=')
                print("Password harus memiliki 8-20 karakter")
                print(50*'=')

    elif opsi == 6:
        print('Sampai jumpa lagi')
        break
