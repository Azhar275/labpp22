matriksA= [[int(input(f'Masukkan matriks pertama indeks {j},{i} : ')) for i in range(1, 3)] for j in range(1,3)]
matriksB= [[int(input(f'Masukkan matriks kedua indeks {j},{i} : ')) for i in range(1, 3)] for j in range(1,3)]

hasil= [[0,0], [0,0]]
hasil[0][0] = (matriksA[0][0] * matriksB[0][0]) + (matriksA[0][1] * matriksB[1][0])
hasil[0][1] = (matriksA[0][0] * matriksB[0][1]) + (matriksA[0][1] * matriksB[1][1])
hasil[1][0] = (matriksA[1][0] * matriksB[0][0]) + (matriksA[1][0] * matriksB[1][0])
hasil[1][1] = (matriksA[1][0] * matriksB[0][1]) + (matriksA[1][1] * matriksB[1][1])

print(f"| {matriksA[0][0]}, {matriksA[0][1]} | X | {matriksB[0][0]}, {matriksB[0][1]} | = | {hasil[0][0]}, {hasil[0][1]} |")
print(f"| {matriksA[1][0]}, {matriksA[1][1]} |   | {matriksB[1][0]}, {matriksB[1][1]} |   | {hasil[1][0]}, {hasil[1][1]} |")