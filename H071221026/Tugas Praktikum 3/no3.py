price= int(input("input price : "))
pay= int(input("input money : "))
kembalian= pay-price

money= [100000,50000,20000,10000,5000,2000,1000]

for i in money :
    pembagian_kembalian= kembalian//i
    print(f"{int(pembagian_kembalian)} uang Rp. {i}")
    kembalian= kembalian-(pembagian_kembalian*i)