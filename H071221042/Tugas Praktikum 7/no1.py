import re

x= input()
y= re.search("^[a-zA-Z02468]{40}[13579 ]{5}$", x)

if y:
    print('true')
else:
    print('false')