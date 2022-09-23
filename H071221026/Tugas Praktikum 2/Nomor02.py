print("===DAFTAR GOLONGAN LISTRIK===")
print("R1")
print("R2")
print("R3")
print("B2")
print("B3")
print("I3")
print("P1")

golongan= str(input("Masukkan Golongan Anda : ").upper())
daya= float(input("Masukkan daya listrik anda (dalam VA) : "))
pemakaian= float(input("Masukkan total pemakian listrik anda : "))

if golongan == 'R1' :
    if daya == 900 :
        print (f"jumlah tagihan anda : {pemakaian*1352:,}")
    elif daya>=1300 and daya<=2200 :
        print (f"jumlah tagihan anda : {pemakaian*1400.70:,}")
    else :
        print('Data tidak valid')
elif golongan == 'R2' :
    if daya>=3500 and daya<=5500 :
        print (f"jumlah tagihan anda : {pemakaian*1699.53:,}")
    else :
        print('Data tidak valid')
elif golongan == 'R3' :
    if daya>=6600 :
        print (f"jumlah tagihan anda : {pemakaian*1699.53:,}")
    else :
        print('Data tidak valid')
elif golongan == 'B2' :
    if daya>=6600 and daya<=200000 :
        print (f"jumlah tagihan anda : {pemakaian*1444.70:,}")
    else :
        print('Data tidak valid')
elif golongan == 'B3' :
    if daya>200000 :
        print (f"jumlah tagihan anda : {pemakaian*1114.74:,}")
    else :
        print('Data tidak valid')
elif golongan == 'I3' :
    if daya>=200000 :
        print (f"jumlah tagihan anda : {pemakaian*1314.12:,}")
    else :
        print('Data tidak valid')
elif golongan == 'P1' :
    if daya>=6600 and daya<=200000 :
        print (f"jumlah tagihan anda : {pemakaian*1314.12:,}")
    else :
        print('Data tidak valid')
else :
    print('Data tidak valid')