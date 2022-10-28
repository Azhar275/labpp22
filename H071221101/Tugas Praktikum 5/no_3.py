x = list(map(int, input("List 1 : ").split()))
y = list(map(int, input("List 2 : ").split())) ; n = []
for i in x :
    if i in y:
        if i not in n:
            n.append(i)
if len(n) != 0 :
    print(f"Terdapat {len(n)} buah duplikat yaitu = {set((n))}")
else :
    print("tidak ada duplikat")