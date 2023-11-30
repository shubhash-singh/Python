import re

patt = r'(?<=[bcdfghjklmnpqrstvwxyz])[aeiou]{2,}(?=[bcdfghjklmnpqrstvwxyz])'

input_string = input()
m = re.findall(patt, input_string, re.IGNORECASE)
if len(m)>=1:
    for i in m:
        print(i)
else:
    print("-1")