gol = str(input("Golongan ="))
daya = int(input("Daya ="))
use = int(input("Pemakaian ="))

if gol == 'R1' and daya==900:
    tag = use * 1352
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol == 'R1' and daya==1300:
    tag = use * 1444.70
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol == 'R1' and daya==2200:
    tag = use * 1444.70
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol == 'R2' and daya > 5500:  
    print("Data tidak valid") 
elif gol== 'R2' and daya>=3500:
    tag= use*1699.53
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol == 'R3' and daya>=6600:
    tag= use *1699.53
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol == 'B2' and daya > 200000:  
    print("Data tidak valid")
elif gol== 'B2' and daya>=6600:
    tag= use*1444.70
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol== 'B3' and daya> 200000:
    tag= use* 1114.74
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol== 'I3' and daya> 200000:
    tag= use* 1314.12
    print((f"jumlah tagihan anda : {tag:,}"))
elif gol== 'P1' and daya> 200000:
    print("Data tidak valid")
elif gol== 'P1' and daya>=6600:
    tag= use* 1523.28
    print((f"jumlah tagihan anda : {tag:,}"))
else:
    print('Data tidak valid')