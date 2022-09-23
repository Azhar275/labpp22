# tugas praktikum 1

nilai = input("Masukkan angka ke huruf")
nilai = eval(nilai)

if nilai >= 90:
    na = 'A'
elif nilai >= 80:
    na = 'B'
elif nilai >= 70:
    na = 'C'
elif nilai >= 60:
    na = 'D'
elif nilai >= 40:
    na = 'E'
else:
    na = 'F'
print(f'Nilai {nilai} : {na}')