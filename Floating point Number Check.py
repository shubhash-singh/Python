import re

pattern = r"^[+-]?\d*\.\d+$"

'''
^ checks for start of string
[+-]? checks for any positive or negative sign at starting
\d* checks for zero or more occurance of any digit before dot(.)
\. checks for one occurance of dot(.)
\d+  checks for atleast 1 occurance of digit value after dot(.)

'''
for i in range(int(input())):
    float_input = input()
    if re.match(pattern, float_input):
        print(True)
    else:
        print(False)
        
        