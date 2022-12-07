a = input()
b = input()
try:
    with open (a+'.txt', 'r') as file :
        print(file.read())
        a = file.read()
        b = file.read()

    with open (b+'.txt', 'w') as file :
        file.write(b)

    print ('Berhasil')

except FileNotFoundError :
    print ('Gagal')