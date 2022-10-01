x = int(input('Masukkan angka: '))
y = int(input('Masukkan angka: '))
if y%x!=0:
    line = int((y//x)+1)
elif y%x==0:
    line = int((y/x))
listy = []
for i in range (1,y+1):
    listy.append(i)
for k in range (0,line):
    tp = (listy[k*x:(k*x)+x])
    listToStr = ' '.join([str(l) for l in tp])
    print (listToStr)

for i in range (1, y+1):
    print (i, end=' ')
    if i% x ==0:
        print()