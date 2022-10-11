n= int(input('input n : '))
a= 0
b= 1
sum= 0
for i in range (0,n):
    print (sum, end=' ')
    a=b
    b=sum
    sum=a+b