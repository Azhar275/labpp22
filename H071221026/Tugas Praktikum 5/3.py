array1= list(map(int, input("Input array ke-1 : ").split(" ")))
array2= list(map(int, input("Input array ke-2 : ").split(" ")))
irisan= []
for i in array2 :
    if i in array1 :
        if i not in irisan : 
            irisan.append(i)


arrays= tuple(irisan)
print(f"Terdapat {len(irisan)} duplikat yaitu : {arrays}")