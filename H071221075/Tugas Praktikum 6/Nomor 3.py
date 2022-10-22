x , y = input()+'.txt', int(input())
try:
    with open("Tabel.txt", "r") as tabel:
        file_as = tabel.read()
        with open(x, "w") as konten:
            konten.write(file_as)
            for i in range(y):
                a,b,c = input().replace(" ", "_"), input(), input()
                if len(a) <= 20 and len(b) <= 11 and len(c) <= 4:
                    konten.write(f"|{a.ljust(31)}|{b.ljust(14)}|{c.ljust(12)}|\n+-------------------------------+--------------+------------+\n")
                else:
                    raise Exception()
except: print("Gagal!")
