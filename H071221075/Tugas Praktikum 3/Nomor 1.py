y = int(input("Horizontal : "))
x = int(input("Range : "))
if x > y:
    for i in range(1, x + 1):
        print(i, end=" ")
        if i % y  == 0:
            print()
else:
    print("Tidak Valid!")

        
