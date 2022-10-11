def myDay(usia_hari) :
    year= usia_hari//365 
    day_remaind= usia_hari%365
    month= day_remaind//30
    days= day_remaind%30
    print(f"{year} Tahun")
    print(f"{month} Bulan")
    print(f"{days} Hari")

usia_hari= int(input("masukkan usia dalam hari : "))
myDay(usia_hari)