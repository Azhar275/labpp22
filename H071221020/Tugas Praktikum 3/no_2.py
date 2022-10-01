x = int(input('Masukkan angka: '))
listx = [0,1]
kosong =[]
for i in range (0,x):
    a = [listx[0],listx[1]]
    b = listx[0]+listx[1]
    c = [listx[1],b]
    d = listx[1]+b
    listx.remove(listx[0])
    listx.insert(0,b)
    listx.remove(listx[1])
    listx.insert(1,d)
    listc = [str(j) for j in c]
    kosong.append(listc)
    isi = [i for listc in kosong for i in listc]
    #joinc = str(' '.join(listc))
    #print (jo
    # inc, end=' ')
    isi.insert(0,'0')
print (' '.join(isi[0:x]))

a = 0
b = 1
count=1
sum=0

while count<=x:
    count+=1
    print (sum, end=' ')
    a=b
    b=sum
    sum=a+b
print()
a = 0
b = 1
sum=0
for i in range(0,x):
    print (sum, end=' ')
    a=b
    b=sum
    sum=a+b