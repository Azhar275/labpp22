print('Selamat datang untuk mulai silahkah masukkan data anda')
n= input("Nama: ")
u= input("Umur: ")
a= input("Alamat: ")
data= {
    "Nama": n,
    "Umur": u,
    "Alamat": a
}
while True:
    print("======================================================")
    print(f"Selamat datang {data['Nama']} silahkan pilih opsi")
    print("======================================================")
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print("======================================================")
    x= input("Input opsi: ")
    print("======================================================")

    if x=='1':
        print('Data anda adalah')
        print(f'Nama:', data["Nama"])
        print(f'Umur:', data["Umur"])
        print(f'Alamat:', data["Alamat"])
    elif x=='2':
        a= input('Silahkan input nama baru: ')
        data["Nama"]= a
        print('Data anda sukses di perbaharui')
    elif x=='3':
        b= input('Silahkan input umur baru: ')
        data["Umur"]= b
        print('Data anda sukses di perbaharui')
    elif x=='4':
        c= input('Silahkan input alamat baru: ')
        data["Alamat"]= c
        print('Data anda sukses di perbaharui')
    elif x=='5':
        print(f'Selamat tinggal {data["Nama"]}')
        break
    else:
        print('Opsi tidak ada')