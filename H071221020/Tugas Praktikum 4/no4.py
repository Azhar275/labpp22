# def robot(a):
#     a=input()
#     if a=='u':
#         y=y+1
#         print(y)
#         # print(f'{x}, {y}')
#     elif a=='l':
#         x=x-1
#         print({x}, {y})
#     elif a=='r':
#         x=x+1
#         print({x}, {y})
#     elif a=='d':
#         y=y-1
#         print({x}, {y})
#     else:
#         print()
# robot(a)

def robot(x,y):
    while True:
        a=input().lower()
        if a=='end':
            break
        else:
            a=list(a)
        for i in a:
            if i=='u':
                y=y+1
                print(f'{x}, {y}')
            elif i=='l':
                x=x-1
                print(f'{x}, {y}')
            elif i=='r':
                x=x+1
                print(f'{x}, {y}')
            elif i=='d':
                y=y-1
                print(f'{x}, {y}')
            else:
                continue
robot(0,0)
print('Program Selesai')