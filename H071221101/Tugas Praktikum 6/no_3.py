x , y = input()+'.txt', int(input())
try :
    with open("Tabel.txt", "r") as tabel:
         file_as = tabel.read()
    with open(x, "w") as konten:
            konten.write(file_as)

            for i in range(y):
                a = str(input()).replace(" ","_")
                if len(a) > 20 :
                    print("Nama tidak boleh lebih dari 20 karakter!")
                    raise Exception()
                b = str(input())
                if len(b) > 10 :
                    print("Nim tidak boleh lebih dari 10 karakkter!")
                    raise Exception()
                c = str(input())
                if len(c) > 4 :
                    print("Tahun hanya bisa ditulis dengan 4 karakter")
                    raise Exception()
                konten.write(f"|{a}{' ' * (31 - len(a))}|{b}{' ' * (14 - len(b))}|{c}{' ' * (12 - len(c))}|\n+-------------------------------+--------------+------------+\n")
            print("Berhasil")
except :
    print("Gagal")