x= int(input())
y= int(input())

def get_FPB(x, y):
    if x==0 or y==0:
        return max(x, y)
    for i in range(1,min(x,y)+1):
        if x % i==0 and  y % i==0:
            fpb= i
    return fpb

print (f'FPB ({x},{y})=', get_FPB(x, y))