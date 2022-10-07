def getFPB(x,y):
    # lx=[]
    # for i in range(1,x):
    #     if (x/i)%1==0:
    #         lx.append(i)
    # ly=[]
    # for j in range(1,y):
    #     if (y/j)%1==0:
    #         ly.append(j)
    # inter=[k for k in lx if k in ly]
    # print(f'FPB({x}, {y}) = {inter[-1]}')
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            if x==0 or y==0:
                i=abs(x-y)
            fpb=i
    print (fpb)
x=int(input())
y=int(input())
getFPB(x,y)