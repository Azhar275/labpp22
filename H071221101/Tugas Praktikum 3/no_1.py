x = int(input("masukkan jumlah kolom : "))
y = int(input("masukkan angka : "))

for i in range(1, y+1):
    print(i, end="\n")
    if i % x == 0 :
        print()