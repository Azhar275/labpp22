def fungsi_perpindahan(perintah,x,y):
    for i in (perintah):
        if i == 'R':
            x = x+1
        elif i == 'L':
            x = x-1
        elif i == 'U':
            y= y+1
        elif i == 'D':
            y = y-1
        print(x, y)
    return x, y

x= 0
y= 0
while True:
    perintah= str(input("Masukkan Perintah: "))
    perintah= perintah.upper()
    if perintah=='END':
        print('Program Selesai')
        break
    print(x, y)
    x, y= fungsi_perpindahan(perintah,x,y)