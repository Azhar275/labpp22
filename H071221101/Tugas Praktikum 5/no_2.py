print("Selamat Datang ^^!")
print("Silahkan input data Anda!")
nama = input("Input nama : ")
umur = int(input("Input umur (dalam angka) : "))
alamat = input("Input alamat : ")

dict_data = {
    "nama" : nama,
    "umur" : umur,
    "alamat" : alamat
}

while True :
    print("-"*30)
    print(f"Selamat Datang ^^! {dict_data ['nama']}, silahkan pilih opsi!")
    print("-"*30)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("-"*30)
    opsi = input("Input opsi : " )
    if opsi == "1" :
        print("Data Anda adalah")
        print(f"Nama : {dict_data.get ('nama')}")
        print(f"Umur : {dict_data.get ('umur')}")
        print(f"Alamat : {dict_data.get ('alamat')}")
    elif opsi == "2" :
        rename = input("Silahkan input nama baru : ")
        dict_data['nama'] = rename
        print("Data Anda telah diperbarui! ^^")
    elif opsi == "3" :
        rename = input("Silahkan input umur baru : ")
        dict_data['umur'] = rename
        print("Data Anda telah diperbarui! ^^")
    elif opsi == "4" :
        rename = input("Silahkan input Alamat baru : ")
        dict_data['alamat'] = rename
        print("Data Anda telah diperbarui! ^^")
    elif opsi == "5" :
        print(f"Selamat Tinggal {dict_data['nama']} ^^!")
        break
    else :
        print("opsi salah") 
    