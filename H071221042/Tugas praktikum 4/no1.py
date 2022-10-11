angka= int(input())

def hitung_faktorial (angka):
    if angka > 0:
        return angka*hitung_faktorial(angka-1)
    elif angka == 0:
        return 1
    else:
        print('Tidak Terdefinisi')
        
print(hitung_faktorial(angka))