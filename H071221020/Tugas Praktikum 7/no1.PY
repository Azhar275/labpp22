#AAAAAAAAAAbbbbbbbbbb2222222222444444444413 57
#adfhladkjfhladdfs697adfs86ad7f69a9sdf876
import re
x=input()
bag1=x[0:40]
bag2=x[40:46]
pat1='^(([a-zA-Z]|(2|4|6|8|0)){40})$'
pat2='((([\s1359])){5})$'
res1=re.match(pat1,bag1)
res2=re.match(pat2,bag2)
if res1 and res2:
    print('true')
else:
    print('false')
