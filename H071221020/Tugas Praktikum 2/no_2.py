cat = input('Masukkan kategori listrik anda'.ljust(40)+':')
cat = cat.upper()
p = int(input('Masukkan daya listrik anda'.ljust(40)+':'))
use = float(input('Masukkan pemakaina listrik anda'.ljust(40)+':'))
print (50 * '=')
if p == 900 and cat=='R1':
    print ('Golongan listrik'.ljust(40)+':R1')
    print ('Tarif per kWh'.ljust(40)+':Rp1,352')
    print (f'Jumlah tagihan listrik anda : Rp{use*1352:,}')
elif p == 1300 and cat=='R1':
    print ('Golongan listrik'.ljust(40)+':R1')
    print ('Tarif per kWh'.ljust(40)+':Rp1,440.70')
    print (f'Jumlah tagihan listrik anda : Rp{use*1440.7:,}')
elif p == 2200 and cat=='R1':
    print ('Golongan listrik'.ljust(40)+':R1')
    print ('Tarif per kWh'.ljust(40)+':Rp1,440.70')
    print (f'Jumlah tagihan listrik anda : Rp{use*1440.7:,}')
elif p>=3500 and p<=5500 and cat=='R2':
    print ('Golongan listrik'.ljust(40)+':R2')
    print ('Tarif per kWh'.ljust(40)+':Rp1,699.53')
    print (f'Jumlah tagihan listrik anda : Rp{use*1699.53:,}')
elif p>=6600 and cat=='R3':
    print ('Golongan listrik'.ljust(40)+':R3')
    print ('Tarif per kWh'.ljust(40)+':Rp1,699.53')
    print (f'Jumlah tagihan listrik anda : Rp{use*1699.53:,}')
elif p>=6600 and p<=200000 and cat=='B2':
    print ('Golongan listrik'.ljust(40)+':B2')
    print ('Tarif per kWh'.ljust(40)+':Rp1,444.70')
    print (f'Jumlah tagihan listrik anda : Rp{use*1444.70:,}')
elif p>200000 and cat=='B3':
    print ('Golongan listrik'.ljust(40)+':B3')
    print ('Tarif per kWh'.ljust(40)+':Rp1,114.74')
    print (f'Jumlah tagihan listrik anda : Rp{use*1114.74:,}')
elif p>=200000 and cat=='I3':
    print ('Golongan listrik'.ljust(40)+':I3')
    print ('Tarif per kWh'.ljust(40)+':Rp1,314.12')
    print (f'Jumlah tagihan listrik anda : Rp{use*1314.12:,}')
elif p>= 6600 and p<=200000 and cat=='P1':
    print ('Golongan listrik'.ljust(40)+':P1')
    print ('Tarif per kWh'.ljust(40)+':Rp1,523.28')
    print (f'Jumlah tagihan listrik anda : Rp{use*1523.28:,}')
else:
    print ('Data tidak valid')