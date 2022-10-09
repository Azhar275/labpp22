# Cara Kedua
def FPB(num1, num2):
    new = []
    for i in range(1,num1):
        if min(num1, num2) == 0:
            new.append(str(max(num1, num2)))
        elif num1 % i == 0 and num2 % i == 0:
            new.append(str(i))
    print(f"FPB dari ({num1},{num2}) = {''.join(new[-1])}")
FPB(9 , 0)
# Cara Pertama
def FPB(num1, num2):
    fpb = 0
    for i in range(1,num1):
        if min(num1, num2) == 0:
            fpb = max(num1,num2)
        elif num1 % i == 0 and num2 % i == 0:
            fpb = i
    print(f"FPB dari ({num1},{num2}) = {fpb}")
FPB(72, 64)

