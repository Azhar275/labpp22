x= str(input())
y= str(input())

'''PROGRAM MENYALIN FILE'''
try:
    file1= open(f"{x}.txt")
    isi_file1= file1.readlines()
    isi_file1[-1]+= '\n'
    

    panjang=0
    for i in isi_file1:
        if len(i) > panjang:
            panjang=len(i)

    file2= open(f"{y}.txt", "w")
    for i in isi_file1:
        
        file2.write(i.rjust(panjang))
    print("Berhasil")
except:
      print("Gagal")

