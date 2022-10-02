degree = float(input("Enter Degree: "))
time = (1 / 15) * 3600 * degree
print(time)

clock = time // 3600
C = time % 3600
minute = C // 60
second = C % 60
o = (clock + 6)

if o >= 0 and o <= 11:
    print("Selamat Pagi!") 
elif o > 11 and o <= 15:
    print("Selamat Siang!")
elif o > 15 and o <= 18:
    print("Selamat Sore!")
elif o > 18 and o <= 24:
    print("Selamat Malam!")
print("%02d:%02d:%02d" % ((clock + 6) % 24, minute, second))