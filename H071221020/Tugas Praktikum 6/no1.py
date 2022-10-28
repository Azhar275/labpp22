x=input()
y=input()
d=1
n=str(x+'.txt')
m=str(y+'.txt')
if x==y:
    m=str(y+str(d)+'.txt')
    d=d+1
try:
    with open(n+'.txt') as fi:
        c=fi.read()
    with open(m,'w') as file:
        file.write(c)
    print('Berhasil')
except:
    print('Gagal')