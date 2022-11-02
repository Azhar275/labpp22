import re
def match_IPv4(string):
    #                250-255  200-249    100-199     0-99  
    pola_0to255 = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    pola_IPv4 = fr"{pola_0to255}"+fr".{pola_0to255}"*3
    return re.fullmatch(pola_IPv4,string)

def match_IPv6(string):
    hex_4char = r"[0-9A-Fa-f]{1,4}"
    pola_IPv6 = fr"{hex_4char}"+fr":{hex_4char}"*7
    return re.fullmatch(pola_IPv6,string)

# handling input jumlah ip address
try:
    count = int(input("jumlah inputan : "))
except:
    print("error : pastikan inputan berupa bilangan positif")
else : 
    # jika input jumlah valid

    # minta input ip address sebanyak count
    list_ip_address = []
    for i in range(count): 
        input_ip = input(f"masukkan ip ke{i+1} :")
        list_ip_address.append(input_ip)
        
    # cek jenis tiap inputnya (IPv4/IPv6/None)
    for ip_address in list_ip_address:
        if match_IPv4(ip_address):
            print("IPv4")
        elif match_IPv6(ip_address):
            print("IPv6")
        else:
            print("Bukan IP Address")