
# Cara Panjang
total, tunai = int(input("Total : ")), int(input("Uang Tunai : "))
kembalian = tunai - total
q,w,e,r,t,y,u = 0,0,0,0,0,0,0
while True:
    if kembalian - 100000 >= 0:
        kembalian -= 100000
        q += 1
    elif kembalian - 50000 >= 0:
        kembalian -= 50000
        w += 1
    elif kembalian - 20000 >= 0:
        kembalian -= 20000
        e += 1
    elif kembalian - 10000 >= 0:
        kembalian -= 10000
        r += 1
    elif kembalian - 5000 >= 0:
        kembalian -= 5000
        t += 1
    elif kembalian - 2000 >= 0:
        kembalian -= 2000
        y += 1
    elif kembalian - 1000 >= 0:
        kembalian -= 1000
        u += 1
    else:
        break
print("{} uang Rp 100.000\n{} uang Rp  50.000\n{} uang Rp  20.000\n{} uang Rp  10.000\n{} uang Rp   5.000\n{} uang Rp   2.000\n{} uang Rp   1.000".format(q,w,e,r,t,y,u))

# Cara Pendek
total, tunai = int(input("Total : ")), int(input("Uang Tunai : "))
kembalian = tunai - total
uang = [100000,50000,20000,10000,5000,1000]
for i in uang:
    bagi = kembalian // i
    print("%d uang Rp %d" % (bagi, i))
    kembalian -= bagi * i