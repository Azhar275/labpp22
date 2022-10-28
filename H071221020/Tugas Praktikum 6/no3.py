try:
    fi=input() #nama file
    fi=fi+'.txt' #nama file berekstensi
    co=int(input()) #jumlah unputan
    count=1 #menghitung while
    tab_list=[]
    while count<=co:
        el_list=[]
        na=input() #nama
        na=na.replace(' ','_')
        if len(na)>20:
            print('Karakter nama yang anda masukkan terlalu panjang')
            raise Exception()
        el_list.append(na)
        ni=input() #nim
        if len(ni)>10:
            print('Karakter NIM yang anda masukkan terlalu panjang')
            raise Exception()
        el_list.append(ni)
        ak=input() #angkatan
        if len(ak)>4:
            print('Karakter tahun yang anda masukkan terlalu panjang')
            raise Exception()
        el_list.append(ak)
        tab_list.append(el_list)
        count+=1
    with open(fi,'w') as file: #buat file baru untuk diisi
        file.write('+'+20*'-'+'+'+15*'-'+'+'+10*'-'+'+'+'\n')
        file.write('|'+'Nama'.center(20)+'|'+'NIM'.center(15)+'|'+'Angkatan'.center(10)+'|'+'\n')
        file.write('+'+20*'-'+'+'+15*'-'+'+'+10*'-'+'+'+'\n')   
        for k in tab_list:
            file.write('|'+k[0].ljust(20)+'|'+k[1].ljust(15)+'|'+k[2].ljust(10)+'|'+'\n')
            file.write('+'+20*'-'+'+'+15*'-'+'+'+10*'-'+'+'+'\n')
    print('Berhasil')
except:
    print('Gagal')