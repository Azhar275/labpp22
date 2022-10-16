print("selamat datang untuk memulai silahkan input data anda")
nama= input("Input nama : ")
umur= int(input("input umur : "))
alamat= input("Input alamat : ")

dict_profile= {
    "nama": nama,
    "umur": umur,
    "alamat": alamat
}

while True :
    print("="*60)
    print(f"selamat datang {dict_profile['nama']}, silahkan pilih opsi")
    print("="*60)
    print("1. Detail anda")
    print("2. ubah nama")
    print("3. Ubah umur")
    print("4. ubah alamat")
    print("5. keluar")
    print("="*60)
    opsi= input("input opsi : ")
    print("="*60)    
    if opsi=="1" :
        print("Data anda adalah")
        print(f"Nama : {dict_profile.get('nama')}")
        print(f"Umur : {dict_profile.get('umur')}")
        print(f"Alamat : {dict_profile.get('alamat')}")
    elif opsi=="2" :
        rename= input("Silahkan input nama baru : ")
        dict_profile['nama']= rename
        print("data anda sukses diperbarui")
    elif opsi=="3" :
        reage= input("Silahkan input umur baru : ")
        dict_profile['umur']= reage
        print("data anda sukses diperbarui")
    elif opsi=="4" :
        readress= input("Silahkan input alamat baru : ")
        dict_profile['alamat']= readress
        print("data anda sukses diperbarui")
    elif opsi=="5" :
        print(f"selamat tinggal {dict_profile['nama']}")
        break
    else :
        print("opsi salah")

