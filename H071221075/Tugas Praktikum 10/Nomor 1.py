import re
from prettytable import PrettyTable
_Data = []
while True:
    print("""PILIHAN LAYANAN
1. Detail Anda
2. Ubah Nama
3. Jumlah Data Pada File
4. Save Data pada File
5. Buat Data Baru
6. Keluar """)
    _inputan = int(input("Pilihan : "))
    if _inputan == 1: # Menampilkan Data Diri yang ada dalam list _Data
        if len(_Data) > 0: 
            for i in range(len(_Data)):
                for y in range(len(_Data[0])):
                    print(f'{_Data[i][y]}')
                    if y == 2:
                        print("="*100)
        else:
            print("Data saat ini kosong!\n",100*"=")
    elif _inputan == 2: # Mengubah nama dalam list _Data
        if len(_Data) != 0:
            for i in range(len(_Data)):
                for y in range(len(_Data[0])):
                    if y == 1 or y == 2: 
                        continue
                    print(f'Urutan {i+1} {_Data[i][y]}')
            _newName = list(map(str, input("Masukkan Index dan nama baru (Urutan NamaBaru) : ").split()))
            _Data[int(_newName[0])-1][0] = "Nama : "+_newName[1]
        elif len(_Data) == 0:
            print("Data Tidak Ditemukan!\n", 100*"=")
    elif _inputan == 3: # Menampilkan jumlah data pada file <namaFile>.txt
        _file = input("Masukkan fIle : ")+".txt"
        try:
            with open(_file) as baca:
                dataFILE = re.findall(r"@student.unhas.ac.id", baca.read())
            print(f"Jumlah Data adalah {dataFILE.count('@student.unhas.ac.id')}")
        except FileNotFoundError:
            print(f"Tidak Terdapat File Dengan Nama {_file}")
            print("Jumlah data pada file = 0\n", 100*"=")
    elif _inputan == 4: # Menulis data pada list ke File <namaFile>.txt
        if len(_Data) == 0: 
            print("Data Sata Ini Kosong!\n", 100*"=")
        else:
            _FILE = input("Nama File : ")+".txt"
            tabel = PrettyTable(["Data Tersimpan"])
            tabel.align = "l"
            with open(_FILE, "a") as tulis:
                for i in range(len(_Data)):
                    for y in range(len(_Data[0])):
                        tabel.add_row([_Data[i][y]])
                tulis.write(str(tabel))
                _Data = []
    elif _inputan == 5: # Memasukkan data baru kedalam list _Data
        nama = input("Nama : ")
        _cekEmail = "Not-Clear"
        while _cekEmail == "Not-Clear":
            Email = input("Email : ")
            if re.search(r"^[^A-Z_/-]{1,}@student.unhas.ac.id$", Email):
                _cekEmail = "Clear"
            else:
                print("Email Yang Anda Masukkan salah\n", 100*"=")
        _cekPass = "Not-Clear"
        while _cekPass == "Not-Clear":
            _Pass = input("Masukkan Password : ")
            if len(_Pass) > 8:
                if re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', _Pass):
                    _cekPass = "Clear"
                else:
                    print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka\n", 100*"=")
            else: 
                print("Password Harus Memiliki 8-20 Karakter\n", 100*"=")
            _Data.insert(len(_Data), ["Nama : " + nama,"E-mail : "+ Email, "Password : "+ _Pass])
    elif _inputan == 6: # Keluar dari program/menyelesaikan while
        print("Sampai Jumpa Lagi\n", 100*"=")
        False