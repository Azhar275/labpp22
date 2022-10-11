print('---Menentukan FPB---')

def menentukan_fpb(a, b) :
    if a>b :
        bilangan_terkecil= b
    elif b>a :
        bilangan_terkecil= a
    else :
        bilangan_terkecil= a or b

    if a == 0 :
        fpb= b
    elif b == 0 :
        fpb= a 
    elif a==0 and b==0 :
        fpb= 0
    for i in range(1, bilangan_terkecil+1) :
        if (a%i==0) and (b%i==0) :
            fpb=i
    return fpb

a= int(input("Masukkan bilangan a : "))
b= int(input("Masukkan bilangan b : "))
print(f"FPB ({a}, {b}) = {menentukan_fpb(a,b)}")
