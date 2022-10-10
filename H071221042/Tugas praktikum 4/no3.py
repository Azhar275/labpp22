usia= int(input())

def myDay(usia):
    if usia>0:
        tahun= usia//365
        sisa_= usia-365*tahun
        bulan=sisa_//30
        hari= sisa_-(30*bulan)
        print(tahun, 'tahun')
        print(bulan, 'bulan')
        print(hari, 'hari')
    else:
        print('Salah')
myDay(usia)