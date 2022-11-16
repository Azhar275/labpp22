while True:
    print(""""
1. Detail Anda
2. Ubah Nama
3. Jumlah Data Pada File
4. Save Data pada File
5. Buat Data Baru
6. Keluar
    """)
    _inputan = int(input(" "))
    if _inputan == 1:
        print("Jumlah data :") if jumlahdata > 0 else print("Data saat ini kosong!")
    elif _inputan == 2:
        _Nama = input("") if jumlahdata > 0 else print("Data saat ini kosong!")
    elif _inputan == 3:
        _file = input("Masukkan fle")+".txt"
        try:
            print("Jumlah Data adalah")
        except FileNotFoundError:
            print(f"Tidak Terdapat File Dengan Nama {_file}")
    elif _inputan == 4:

