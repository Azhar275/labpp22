print("*NILAI X>Y")
x= int(input("Input X : "))
y= int(input("Input Y : "))

if x<y :
    for i in range(1, y+1) :
        print(i, end=" ")
        if i%x == 0 :
            print()
elif x>y :
    print('input error, x harus lebih kecil dari y')