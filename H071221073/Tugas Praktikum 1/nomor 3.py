nilai = float(input("Rata rata pemakaian listrik harian (Wh): "))
tarif = 1325 #Dalam Kwh


harian = float (nilai/1000) #mengubah wh ke Kwh
bulanan = float(harian * 30)
harga = float(bulanan * tarif)

print("jumlah tagihan listrik bulanan : Rp.", round(harga , 2))