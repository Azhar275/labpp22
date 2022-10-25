tst, sts = input("")+'.txt', input("")+'.txt'
try:
    with open(tst) as f:
        file = f.read()
        with open(sts, "w") as salinan:
            salinan.write(file) 
            print("Berhasil") 

except: 
    print("Gagal")
