nama_file= input("Masukkan nama file : ")
salinan= input("Masukkan nama file salinan : ")

try : 
    with open(f"{nama_file}.txt", "r") as file_asli :
        baca= file_asli.read()
except :
    print("Gagal")
else :
    with open(f"{salinan}.txt", "w") as copy :
        copy.write(baca)
    print("Berhasil")