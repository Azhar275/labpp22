def creatMat2d(x,y) :
    data = []
    for i in range(x) :
        kal = []
        for k in range(y) :
            isi = int(input("matriks [{},{}] = ".format(i,k)))
            kal.append(isi)
        data.append(kal)
    return data

def perkalian(A,B) :
    hasil = []
    for y in range(2) :
        total = []
        for x in range(2) :
            kali = A[y][0]*B[0][x] + A[y][1]*B[1][x]
            print(kali)
            total.append(kali)
        hasil.append(total)
        print(hasil)
    return hasil

matriks = creatMat2d(2,2)
print("matriks 1 =", matriks)
matriksx1 = creatMat2d(2,2)
print("matriks 2 =", matriks)

kali = perkalian(matriks, matriksx1)
print("matriks 1 x matriks 2 =", kali)