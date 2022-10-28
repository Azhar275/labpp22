# ukuran = int(input("Ukuran Matriks : "))
# matriks_1 = [[int(input(f"Matriks 1 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran)] for baris in range(ukuran)]
# matriks_2 = [[int(input(f"Matriks 2 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran)] for baris in range(ukuran)]
# matriks_3 = [[0 for kolom in range(ukuran)] for baris in range(ukuran)] 

matriks_1 = []
for i in range(2):
    baris = []
    for j in range(2):
        baru = int(input(f"Matriks 1 Baris {i + 1} dan Kolom {j + 1} : "))
        baris.append(baru)
    matriks_1.append(baris)
print(matriks_1)

matriks_2 = []
for i in range(2):
    baris = []
    for j in range(2):
        baru = int(input(f"Matriks 2 Baris {i + 1} dan Kolom {j + 1} : "))
        baris.append(baru)
    matriks_2.append(baris)
print(matriks_2)

a3 = (matriks_1[0][0]*matriks_2[0][0]) + (matriks_1[0][1]*matriks_2[1][0])
c3 = (matriks_1[1][0]*matriks_2[0][0]) + (matriks_1[1][1]*matriks_2[1][0])
b3 = (matriks_1[0][0]*matriks_2[0][1]) + (matriks_1[0][1]*matriks_2[1][1])
d3 = (matriks_1[1][0]*matriks_2[0][1]) + (matriks_1[1][1]*matriks_2[1][1])
# print ()
print(f'| {matriks_1[0][0]}, {matriks_1[0][1]} | x | {matriks_2[0][0]}, {matriks_2[0][1]} | = | {a3}, {b3} |')
print(f'| {matriks_1[1][0]}, {matriks_1[1][1]} |   | {matriks_2[1][0]}, {matriks_2[1][1]} |   | {c3}, {d3} |')

# for x in range(ukuran):
#     for y in range(ukuran):
#         for z in range(ukuran):
#             matriks_3[x][y] += matriks_1[x][z] * matriks_2[z][y]
# print(f"{matriks_1} X {matriks_2} = {matriks_3}")