import re
s= input()
if len(s)==45 :
    pola1= r"(\A([A-Za-z02468]){40})[\s13579]{5}"
    result1= re.match(pola1, s)
    if result1 :
        print("true")
    else :
        print("false")
else :
    print("false")

