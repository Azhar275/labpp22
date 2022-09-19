import math

x,y,h = int(input("sudut elevasi a : ")), int(input("sudut elevasi b : ")), int(input("masukkan tinggi menara : "))
TAN_1,TAN_2=  math.tan(math.radians(x)), math.tan(math.radians(y))

panjang_1 = TAN_1 * h
panjang_2 = TAN_2 * h
p = panjang_1 - panjang_2

if p < 0:
    print("Panjang dari kapal adalah %5.1f" % ((-1) * p))
else:
    print("Panjang dari kapal adalah %5.1f" % (p))