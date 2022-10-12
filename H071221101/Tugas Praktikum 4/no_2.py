def fpb(x,y):
    if (y == 0):
        return x
    else:
        return fpb(y,x % y)
def main():
    x = int(input("masukkan bilangan pertama : "))
    y = int(input("masukkan bilangan kedua : "))
    print("FPB dari",x,"dan",y, "=",fpb(x,y))
main()
