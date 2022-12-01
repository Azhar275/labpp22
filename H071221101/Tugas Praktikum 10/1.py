import re, os

print('='*60)

nama = []
email = []
password = []
jumlah = 0

while True :
    print("="*60)
    print(f"Halo! silahkan pilih opsi : ")
    print("="*60)
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Jumlah data pada file")
    print("4. Save data pada file")
    print("5. Buat data baru")
    print("6. Keluar")
    print("="*60)

    opsi = int(input("Opsi yang diinginkan : "))
    print("="*60)

    if opsi == 1 :
        if len(nama) == 0 or len(email) == 0 or len(password) == 0:
            print("Data saat ini kosong")
        else :
            print("Data anda adalah : ")
            print(f"Nama : {nama}")
            print(f"Email : {email}")
            print(f"Password : {password}")

    elif opsi == 2 :
        if len(nama) == 0 or len(email) == 0 or len(password) == 0:
            print("Data saat ini kosong")
        else : 
            ubah_nama = input("Silahkan input nama baru : ")
            nama = ubah_nama

    elif opsi == 3 :
        print(jumlah)
    

    elif opsi == 4 :
        if nama == [] and email == [] and password == [] :
            print("Data saat ini masih kosong")
        else :
            if not os.path.isfile('Data.txt') :
                with open ('Data.txt', 'w') as file :
                    file.write("=========================================\n")
                    file.write("Data yang Tersimpan\n")
                    file.write("=========================================\n")
                    file.write(f"|Nama : {nama} \n")
                    file.write(f"|Email :{email} \n")
                    file.write(f"|Password : {password} \n")
                    file.write("=========================================\n")
                    jumlah += 1
            file2 = open('Data.txt', 'a')
            file2.write(f"|Nama : {nama} \n")
            file2.write(f"|Email :{email} \n")
            file2.write(f"|Password : {password} \n")
            file2.write("=========================================\n")
            jumlah += 1


    elif opsi == 5 :
        namaBaru = input("Silahkan input nama : ")
        nama = namaBaru

        while True :
            pola = "[a-zA-Z0-9]+@student.unhas.ac.id"
            emailBaru = input("Silahkan input email : ")
            hasil = re.match(pola, emailBaru)
        
            if hasil == None :
                print("Email yang Anda Masukkan Salah")
            else :
                email = emailBaru
                break

        while True :
            passwordBaru = input("Silahkan input password : ")
            
            if re.findall("[A-Z]", passwordBaru) != []:
                if re.findall("[a-z]", passwordBaru) != [] :
                    if re.findall("[0-9]", passwordBaru) != [] :
                        if len(passwordBaru) > 8 and len(passwordBaru) < 20 :
                            print("Password Valid")
                            password = passwordBaru
                            break
            print("="*60)
            print("password salah")
            print("="*60)
            
    elif opsi == 6:
        print('Sampai jumpa lagi')
        break