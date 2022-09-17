import math
h = float (input("Ketinggian menara:"))
a = float (input("ujung belakang kapal:"))
b = float (input("ujung depan kapal:"))

dep = math.tan(math.radians(b))*h
bel= math.tan(math.radians(a))*h
p =  bel-dep
print ("%.2fm"%p)