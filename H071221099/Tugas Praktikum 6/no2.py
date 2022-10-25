x = input("") + ".txt"
y = input("") + ".txt"

try:
    with open(x, "r") as old:
        file_asli = old.readlines()
        nilai = []
        file_asli[-1] += "\n" 
        for x in file_asli:
            nilai.append(len(x)) 
            with open(y, "w") as new:
                for i in file_asli:
                    new.write(i.rjust(max(nilai)))
    print("Berhasil")
except:
    print("Gagal")