harga= int(input())
bayar= int(input())
kembalian= bayar-harga

pecahan=[100000, 50000, 20000, 10000, 5000, 2000, 1000]
if harga<bayar:
    for p in pecahan:
        pecahan= int(kembalian/p)
        kembalian= kembalian- (p * pecahan)
        print (f'{pecahan} uang Rp. {p}')
else:
    print('Uang tidak Cukup')