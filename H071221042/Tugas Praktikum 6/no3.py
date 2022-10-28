from logging import raiseExceptions

x= str(input())

header= open("nomor3.txt")
isi_header=header.read()

try:
    n= int(input())
    file= open(f"{x}.txt", "w")
    file.write(isi_header)

    for i in range(n):
        nama= str(input()).replace(" ", "_")
        if len(nama) > 20:
            print("Nama harus tidak lebih dari 20 karakter")
            raise Exception()
        nim= str(input())
        if len(nim) > 10:
            print("NIM harus kurang dari 10 karater")
            raise Exception()
        angkatan= str(input())
        if len(angkatan) > 4:
            print("Tahun harus 4 karakter")
            raise Exception()
        file.write(f"|{nama.ljust(21)} |{nim.ljust(9)}|{angkatan.ljust(10)}|\n")
    file.write("+----------------------+----------+----------+")
    print("Berhasil")
except:
    print("Gagal")