x=input()
y=input()
d=1
c=''
n=str(x+'.txt')
m=str(y+'.txt')
if x==y:
    m=str(y+str(d)+'.txt')
    d=d+1
try:
    with open(n) as fi:
        c=fi.readlines()
    c[-1]=c[-1]+'\n'
    max_=[]
    for j in c:
        len_=len(j)
        max_.append(len_)
    al=max(max_)
    with open(m,'w') as file:
        for i in c:
            file.write(i.rjust(al))
    print('Berhasil')
except:
    print('Gagal')