print("*NILAI X<Y")
x= int(input("Input X : "))
y= int(input("Input Y : "))
if x<y :
    if y%x != 0 :
        line_total= int((y//x)+1)
    elif y%x == 0 :
        line_total= int((y/x)+1)

    datas= []
    for i in range(1, y+1) :
        datas.append(i)
    for j in range (0, line_total) :
        output= (datas[j*x:(j*x)+x])
        convertion= ' '.join([str(number) for number in output])
        print(convertion)
elif x>y :
    print('input error, x harus lebih kecil dari y')