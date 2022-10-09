def faktorial(angka):
    if angka == 1:
        return angka
    else:
        return angka * faktorial(angka - 1)

bilangan = int(input("masukkan angka: "))
if bilangan == 0:
    print ("1")
elif bilangan < 0:
    bilangan = int (input("masukkan angka (harus lebih dari 0: "))
    print(faktorial(bilangan))
else:
    print (faktorial(bilangan))

