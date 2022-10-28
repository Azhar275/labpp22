m1= []  
for matriks in range (2):
    m1.append([])
    for j in range(2):
        a=int(input(f"Masukkan angka: "))
        m1[matriks].append(a)
m2= []  
for matriks in range (2):
    m2.append([])
    for j in range(2):
        a=int(input("Masukkan angka: "))
        m2[matriks].append(a)
m_hasil=[[0 for x in range (2)] for y in range (2)]
for i in range (2):
    for j in range(2):
        m_hasil[i][j]= m1[i][0]*m2[0][j]+m1[i][1]*m2[1][j]

print(f'{m1} X {m2} = ', m_hasil)