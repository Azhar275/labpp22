import math

print("Note :")
print("1. 90>a>b")
print("2. h : tinggi menara")
print("3. a : Sudut Elevasi terhadap Ujung Depan Kapal")
print("4. b : Sudut Elevasi terhadap Ujung Belakang Kapal")
print("5. c : Sudut Elevasi terhadap Kapal")
print("6. AB : Panjang Kapal")
print("7. BC : jarak kapal ke menara")
print("8. AC : Panjang kapal + jarak kapal ke menara")

h= float(input("Insert tower height = " ))
a= float(input("Angle of elevation with respect to the Forward end of the ship = "))
b= float(input("Angle of elevation with respect to the aft end of the ship = "))

kapal_jarak_menara= math.tan(math.radians(a))*h
jarakKapalkeMenara= math.tan(math.radians(b))*h
panjang_kapal= kapal_jarak_menara-jarakKapalkeMenara

print("Maka Panjang Kapal adalah", round(panjang_kapal, 1), "m")

