a = input()    
b = input()

try:
    with open (a+'.txt', 'r') as file :
        a = file.readlines()
        print(a)

        a[-1] = a[-1]+'\n'
        x = 0
        for i in a:
            if len(i) > x:
                x = len(i)

    with open (b+'.txt', 'w') as file :
        for i in a:
            file.write(i.rjust(x))

    print ('Berhasil')

except FileNotFoundError :
    print ('Gagal')