nama_file= input("Masukkan Nama File : ")
jumlah_asisten= int(input("Masukkan Jumlah asisten : "))
try :
    with open(f"{nama_file}.txt", "w") as table :
        table.write(f"+{'-'*20}+{'-'*15}+{'-'*10}+\n")
        table.write(f"|NAMA{' '*16}|NIM{' '*12}|ANGKATAN{' '*2}|\n")
        table.write(f"+{'-'*20}+{'-'*15}+{'-'*10}+\n")
        for i in range(jumlah_asisten) :
            nama_asisten= input("Nama asisten : ")
            ganti= nama_asisten.replace(' ', '_')
            nim= input("NIM : ")
            angkatan= input("Angkatan : ")
            if len(nama_asisten) <= 20 and len(nim)<=15 and len(angkatan)<=10 :
                table.write(f"|{ganti}{' '*(20-len(ganti))}|{nim}{' '*(15-len(nim))}|{angkatan}{' '*(10-len(angkatan))}|\n")
            else :
                print("inputan tidak boleh melebihi batas")
                raise Exception()
        table.write(f"+{'-'*20}+{'-'*15}+{'-'*10}+\n")
        print("Berhasil")
except :
    print("Gagal")



