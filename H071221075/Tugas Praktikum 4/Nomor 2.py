n = list(map(str,input("Masukkan Kata : ").strip()))
def rotasi(n):
    for i in range(len(n)):
        n.insert(0, n[-1])
        n.pop(-1)
        print(''.join(n), end=" | ")
rotasi(n)