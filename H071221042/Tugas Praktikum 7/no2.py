import re
a= int(input())
ip= []

for i in range(a):
    x= input()
    ip.append(x)
for i in ip:
    z= re.search("^([0-9a-f]{1,4}:){7}([0-9a-f]{1,4})", i)
    y= re.search("^([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5].){3}([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|2[5][0-5])$", i)
    
    if z:
        print('IPv6')
    elif y:
        print('IPv4')
    else:
        print('Bukan keduanya')