# to handle regex error if there is any error in regular expression

import re

for i in range(int(input())):
    a = input()
    try:
        re.compile(a)
        print(True)
    except re.error:
        print(False)