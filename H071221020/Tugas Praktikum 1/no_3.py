from tabulate import tabulate

print (100*'=')
print ("MENGHITUNG GAJI KARYAWAN".center(100))
print (100*"=")

name_salary = []

while True :
    name = input('Nama pegawai'.ljust(30)+':')
    salary = float(input('Gaji pokok'.ljust(30)+':'))
    salary__ = [str(salary), '$']
    salary_ = ' '.join(salary__)
    sell = float(input('Hasil penjualan'.ljust(30)+':'))
    sell__ = ['{:.2f}'.format(sell), '$'] #penjualan dengan 2 desimal
    sell_ = ' '.join(sell__)
    ttl = (salary + (sell*(15/100))) #total gaji
    ttl_dec = ['{:.2f}'.format(ttl), '$'] #total gaji dengan 2 desimal
    total = (' '.join(ttl_dec)) #menggabungkan ttl dan tanda $
    name_salary.append([name,salary_,sell_,total])
    ya = input('Apakah anda ingin menambahkan data lain (1. ya, 2. tidak):')
    ya = ya.lower()
    if ya == '2' :
        break
    else :
        print (50*'-')

col = ['Nama', 'Gaji Pokok', 'Total Penjualan', 'Total Gaji']

print (' ')
print (tabulate(name_salary, headers=col, tablefmt='grid', colalign='left'))
print (' ')

print (100*'=')
print ("TERIMA KASIH".center(100))
print (100*"=")

# while True :
#     inp = input(':')
#     y.append(inp)
#     print (y)
#     ya = input(':')
#     ya = ya.lower()
#     if ya == 'tidak' :
#         break