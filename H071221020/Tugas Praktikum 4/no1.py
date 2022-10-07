def fac(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return (x*fac(x-1))
x=int(input(':'))
print(fac(x))