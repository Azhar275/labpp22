def faktroial(angka) :
    if angka==0 :
        return 1
    else :
        return angka*faktroial(angka-1)
angka= int(input("masukkan angka : "))

if angka >= 0 :
    print(f"{angka} faktorial adalah : {faktroial(angka)}")
else :
    print("angka mines tidak memiliki faktorial")