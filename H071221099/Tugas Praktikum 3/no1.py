x = int(input("Horizontal : "))
y = int(input("Range :"))
if x < y:
    for i in range (1, y + 1):
        print (i, end=" ")
        if i % x == 0:
            print()
else:
    print("inputan no no valid")
