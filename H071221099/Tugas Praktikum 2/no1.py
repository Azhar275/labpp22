#konversi angka ke huruf

x = int(input("nilai: "))

if x >= 90 and x <= 100:
    print ("nilai %s = 'A'" %(x))
elif x >= 80 and x < 90:
    print ("nilai %s = 'B'" %(x))
elif x >= 70 and x < 80:
    print ("nilai %s = 'C'" %(x))
elif x >= 60 and x < 70:
    print ("nilai %s = 'D'" %(x))
elif x >= 40 and x < 60:
    print ("nilai %s = 'E'" %(x))
else:
    print ("nilai %s = 'F'" %(x))