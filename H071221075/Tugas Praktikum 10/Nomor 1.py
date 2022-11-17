import re

_Data = [[]]
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
        print(f"Jumlah data : {len(_Data)}") if _Data > 0 else print("Data saat ini kosong!")
    elif _inputan == 2:
        _Nama = input("") if jumlahdata > 0 else print("Data saat ini kosong!")
    elif _inputan == 3:
        _file = input("Masukkan fle")+".txt"
        try:
            with open(_file) as baca:
                for i in baca:
                    dataFILE = re.findall(r"ac.id", i)
            print(f"Jumlah Data adalah {dataFILE.count('ac.id')}")
        except FileNotFoundError:
            print(f"Tidak Terdapat File Dengan Nama {_file}")
    elif _inputan == 4: 
        if len(_Data) == 0: print("Data Sata Ini Kosong!")
        else:
            _FILE = input("Nama File : ")+".txt"
            with open(_FILE, a) as tulis:
                for i in range(len(_Data)):
                    for y in range(len(_Data[0])):
                        tulis.write(_Data[i][y])


    elif _inputan == 5:
        nama = input("Nama : ") ; _Data.append(nama)
        _cekEmail = "Not-Clear"
        while _cekEmail == "Not-Clear":
            Email = input("Email : ")
            if re.search(r"^[^A-Z_/-]@student.unhas.ac.id$", Email):
                _cekEmail == "Clear"
            else:
                print("Email Yang Anda Masukkan salah")
        _cekPass = "Not-Clear"
        while _cekPass == "Not-Clear":
            Pass = input("Masukkan Password : ")
            if re.search(r"[\w+]{8,20}", Email):
                
                _cekPass == "Clear"
            else:
                print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
    elif _inputan == 6:
        print("Sampai Jumpa Lagi")
        False