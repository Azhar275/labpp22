x= set(input("Input array ke-1: ").split(' '))
y= set(input("Input array ke-2: ").split(' '))

z= x.intersection(y)
v= len(z)
if v==0:
    print('Tidak terdapat duplikat')

elif v>0:
    print(f'Terdapat {v} duplikat yaitu',tuple(map(int, z)))