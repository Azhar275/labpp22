import re
n= int(input('masukkan jumlah baris : '))
listip= []
for i in range(n) :
    ip= input("Masukkan IP : ")
    listip.append(ip)

ipv4= r'(([0-1]?([\d]?){2}|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
ipv6= r'(([\dA-Fa-f]{1,4}?\:){7})([\d,A-F,a-f]{1,4})$'

for j in listip : 
    reasult1= re.match(ipv4, j)
    if reasult1 :
        print("IPv4")
    else :
        reasult2= re.match(ipv6, j)
        if reasult2 :
            print("IPv6")
        else :
            print("Bukan IP Address")