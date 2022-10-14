x=int(input('Masukkan Jumlah Baris dan Kolom: '))
mat1=[[int(input(f'Masukkan matriks pertama baris-{col1+1} kolom-{row1+1}:')) for row1 in range (0,x)] for col1 in range (0,x)]
mat2=[[int(input(f'Masukkan matriks kedua baris-{col2+1} kolom-{row2+1}:')) for row2 in range (0,x)] for col2 in range (0,x)]
mat0=[[0 for z in range(0,x)] for z2 in range(0,x)]
for j in range(len(mat1)):
    for k in range(len(mat2[0])):
        for l in range(len(mat2)):
            mat0[j][k] += mat1[j][l] * mat2[l][k]
print(f'{mat1[0]} x {mat2[0]} = {mat0[0]}')
for i in range(1,x):
    print(f'{mat1[i]}   {mat2[i]}   {mat0[i]}')