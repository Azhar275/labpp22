# Program mencari angka terbesar
a, b, c = int(input("A : ")), int(input("B : ")), int(input("C : "))
if a <= b and c <= b:
    print("%d adalah nilai terbesar" % (b))
elif a <= c and b <= c:
    print("%d adalah nilai terbesar" % (c))
else:
    print("%d adalah nilai terbesar" % (a))

# Menghitung jumlah angka genap, positif, negatif, dan ganjil.
'''''
ganjil, genap, minus, positif = 0,0,0,0
daftar_angka = list(map(int,input("\nEnter the numbers : ").strip().split()))
for i in daftar_angka:
    if i % 2 == 0:
        genap += 1
    if i % 2 == 1:
        ganjil += 1
    if i < 0:
        minus += 1
    if i > 0:
        positif += 1
print("Ganjil : %d, Genap : %d, Positif : %d, Negatif : %d" % (ganjil, genap, positif, minus))
'''''