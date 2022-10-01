x = int(input('Masukkan harga barang: '))
y = int(input('Masukkan jumlah uang: '))
xy = y-x
a = 100000
b= 50000
c = 20000
d = 10000
e = 5000
f = 2000
g = 1000
'''
100
50
20
10
5
2
1
'''

nominal = [100000,50000,20000,10000,5000,2000,1000]
for i in nominal:
    s = xy//i
    print (f'{s} uang Rp.{i:,}')
    xy = xy-(s*i)

A = xy//a
B = (xy%a)//b
C = ((xy%a)%b)//c
D = (((xy%a)%b)%c)//d
E = ((((xy%a)%b)%c)%d)//e
F = (((((xy%a)%b)%c)%d)%e)//f
G = ((((((xy%a)%b)%c)%d)%e)%f)//g
print (A,B,C,D,E,F,G)