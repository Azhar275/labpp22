print('Selamat datang! Untuk memulai silahkan masukkan data anda')
name=input('Input nama: ')
age=int(input('Input umur: '))
addr=input('Input alamat: ')
li=[name,age,addr]
while True:
    print(50*'*')
    print(f'Selamat datang {li[0]}, silahkan pilih opsi')
    print(50*'*')
    print('1. Detail anda')
    print('2. Ubah nama')
    print('3. Ubah umur')
    print('4. Ubah alamat')
    print('5. Keluar')
    print(50*'*')
    ops=int(input('Pilih opsi: '))
    print(50*'*')
    if ops==1:
        print('Data anda adalah')
        print(f'Nama: {li[0]}')
        print(f'Umur: {li[1]}')
        print(f'Alamat: {li[2]}')
    elif ops==2:
        newname=input('Silahkan input nama baru anda: ')
        li.remove(li[0])
        li.insert(li.index(li[0]),newname)
        print('Data anda berhasil diperbaharui')
        print(li)
    elif ops==3:
        newage=int(input('Silahkan input umur baru anda: '))
        li.remove(li[1])
        li.insert(li.index(li[1]),newage)
        print('Data anda berhasil diperbaharui')
        print(li)
    elif ops==4:
        newaddr=input('Silahkan input alamat baru anda: ')
        li[2]=newaddr
        print('Data anda berhasil diperbaharui')
    elif ops==5:
        break
    else:
        print('Masukan inputan yang valid')