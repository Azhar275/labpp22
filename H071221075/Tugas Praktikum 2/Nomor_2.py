gol = input("Golongan Listrik : ")
daya = int(input("Daya Listrik : "))
pemakaian = int(input("Pemakaian : "))
gol = gol.upper()
match gol:
    case "R1":
        if daya == 900: print(f"Jumlah tagihan anda : Rp {pemakaian * 1352}")
        elif daya == 1300 and daya == 2200: print(f"Jumlah tagihan anda : Rp {pemakaian * 1352}")
        else: print("Data Tidak Valid!")
    case "R2":
         print(f"Jumlah tagihan anda : Rp {pemakaian * 1699.53:,}") if daya >= 3500 and daya <= 5500 else print("Data Tidak Valid!")       
    case "R3":
        print(f"Jumlah tagihan anda : Rp {pemakaian * 1699.53:,}") if daya >= 6600 else print("Data Tidak Valid!")
    case "B2":
        print(f"Jumlah tagihan anda : Rp {pemakaian * 1444.70:,}") if daya >= 6600 and daya <= 200000 else print("Data Tidak Valid!")
    case "B3":
        print(f"Jumlah tagihan anda : Rp {pemakaian * 1114.74:,}") if daya >= 200000 else print("Data Tidak Valid!")
    case "I3":
         print(f"Jumlah tagihan anda : Rp {pemakaian * 1314.12:,}") if daya >= 200000 else print("Data Tidak Valid!")
    case "P1":
        print(f"Jumlah tagihan anda : Rp {pemakaian * 1523.28:,}") if daya >= 6600 and daya <= 200000 else print("Data Tidak Valid!")
    case _:
        print("Data Tidak Valid!")

    
    
    
    