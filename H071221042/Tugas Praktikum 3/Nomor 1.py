x= int(input())
y= int(input())

for i in range(1, y+1):
    if x>=y:
        print('x harus lebih kecil dari y')
        break
    print(i, end=" ")
    if i%x==0:
        print()
