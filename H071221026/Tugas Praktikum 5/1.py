matriksA= [[int(input(f'Masukkan matriks pertama indeks {j},{i} : ')) for i in range(1, 3)] for j in range(1,3)]
matriksB= [[int(input(f'Masukkan matriks kedua indeks {j},{i} : ')) for i in range(1, 3)] for j in range(1,3)]

hasil= []
for x in range(0, len(matriksA)) :
    baris= []
    for y in range(0, len(matriksA[0])) :
        total= 0
        for z in range(0, len(matriksA)) :
            total+= (matriksA[x][z]*matriksB[z][y])
        baris.append(total)
    hasil.append(baris)

print(f"| {matriksA[0][0]}, {matriksA[0][1]} | X | {matriksB[0][0]}, {matriksB[0][1]} | = | {hasil[0][0]}, {hasil[0][1]} |")
print(f"| {matriksA[1][0]}, {matriksA[1][1]} |   | {matriksB[1][0]}, {matriksB[1][1]} |   | {hasil[1][0]}, {hasil[1][1]} |")