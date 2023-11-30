import re

input_string = input()
pattern = r"([a-zA-Z0-9])\1"
# regex to check for more than one occurrence of a digit
m = re.search(pattern, input_string)
if m is not None:
    print(m.group(1))
else:
    print("-1")
