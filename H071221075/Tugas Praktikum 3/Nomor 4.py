n = int(input("Tinggi Piramida : "))
n -= 1 ;i = 1
while n >= 0:
    print(" " * n, i * "*" )
    i += 2 ; n -= 1
