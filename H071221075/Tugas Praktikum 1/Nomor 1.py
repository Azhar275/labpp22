import math
x,y,h = int(input("Sudut elevasi a : ")), int(input("Sudut elevasi b : ")), int(input("Masukkan Tinggi menara: "))
TAN_1, TAN_2 = math.tan(math.radians(x)), math.tan(math.radians(y)) ; print(TAN_1) ; print(TAN_2)

Panjang_1 = TAN_1 * h
Panjang_2 = TAN_2 * h
p = Panjang_1 - Panjang_2 ; print(p)
print("Panjang Kapal %5.1f m" % (p))