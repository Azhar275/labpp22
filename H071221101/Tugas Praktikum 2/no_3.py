# tugas praktikum 3

a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

if a >= b and a >= c:
    print(a, 'adalah nilai yang terbesar')
elif b > a and b > c:
    print(b, 'adalah nilai yang terbesar')
else:
    print(c, 'adalah nilai yang terbesar')