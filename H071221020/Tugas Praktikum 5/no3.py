x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = []
for i in y:
    if i in x:
        z.append(i)
z = set(tuple(z))
print(f'Terdapat {len(z)} data yang sama: {z}')