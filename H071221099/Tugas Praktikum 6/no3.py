x = input()+'.txt'
y = int(input())

with open("tabel.txt", "r") as tabel:
    file_as = tabel.read()
    with open(x, "w") as konten:
        konten.write(file_as)
        for i in range(y):
            a = input().replace(" ", "_")
            b = input()
            c = input()
            if len(a) > 20 or len(b) > 10 or len(c) > 4:
                print('gagal')
                exit()
            else:
                konten.write(f"\n|{a.ljust(31)}|{b.ljust(14)}|{c.ljust(12)}|")
        konten.write('\n+-------------------------------+--------------+------------+')
        print("Berhasil")