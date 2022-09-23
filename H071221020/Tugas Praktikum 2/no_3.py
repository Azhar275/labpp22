try :
    x = list(map(int, input(('Masukkan bilangan').ljust(30)+':').split()))

    event=sum(1 for i in x if i%2==0)
    odd=sum(1 for i in x if i%2==1)
    neg=sum(1 for i in x if i<0)
    pos=sum(1 for i in x if i>0)

    print (50 * '=')
    print (f'{event} Angka Genap')
    print (f'{odd} Angka Ganjil')
    print (f'{pos} Angka Positif')
    print (f'{neg} Angka Negatif')
    print (50 * '=')
except :
    print ('Inputan tidak valid')
'''
genap
ganjil
positif
negatif
'''