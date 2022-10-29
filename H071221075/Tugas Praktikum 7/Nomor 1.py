import re
x = input()
print(True) if re.search(r"^[24680a-zA-Z]{40}[13579\s]{5}$", x) else print(False) 