def myDay(x):
    print(f'{x//365} tahun')
    print(f'{(x%365)//30} bulan')
    print(f'{(x%365)%30} hari')
x=int(input())
myDay(x)