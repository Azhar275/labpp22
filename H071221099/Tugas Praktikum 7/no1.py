import re

s = input('')
# print(len(s))

first_regex = r'[02468_]'
sec_regex = r'[13579 ]'

resultone = re.findall(sec_regex, s[0:40])
if resultone:
    print('\nfalse')
    exit()

resultwo = re.findall(first_regex, s[40:45])
if resultwo:
    print('\nfalse')
    exit()

if len(s) == 45:
    print('\ntrue')
else:
    print('\nfalse')