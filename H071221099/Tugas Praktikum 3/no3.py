total, tunai = int(input("Total: ")), int(input("uang tunai: "))
kembalian = tunai - total
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if total < tunai:
    for i in uang:
        bagi = kembalian // i
        print ("%d uang Rp %d" % (bagi, i))
        kembalian -= bagi * i
elif total > tunai:
    print("ngutang dulu di'")
else:
    print("sudah pas yah uangnya ")
