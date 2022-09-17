import math
r = float(input("Jari-jari alas:"))
t = float(input("Tinggi:"))

vol = (1/3)*math.pi*r**2*t
s = math.sqrt(t**2+r**2)
luas= math.pi*r*(r+s)
print ("> volume :","%.2f"%vol)
print ("> Luas permukaan :","%.2f"%luas)