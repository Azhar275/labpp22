nama_file= input("Masukkan nama file : ")
salinan= input("Masukkan nama file salinan : ")

try : 
    with open(f"{nama_file}.txt", "r") as file_asli :
        baca= file_asli.read()
except :
    print("Gagal")
else :
    with open(f"{nama_file}.txt") as garis :
        rata_kanan= garis.readlines()
        rata_kanan[-1]= rata_kanan[-1]+"\n"
    with open(f"{salinan}.txt", "w") as ind :
        nilai_terbesar= len(rata_kanan[0])
        for nilai in rata_kanan :
            if len(nilai)>nilai_terbesar :
                nilai_terbesar=len(nilai)
        for i in rata_kanan :
            ind.write(i.rjust(nilai_terbesar))   
    print("Berhasil")