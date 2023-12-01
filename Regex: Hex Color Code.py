import re

patt = r"#[0-9A-Fa-f]{3,6}"
is_code = False
for i in range(int(input())):
    input_line = input()
    x = input_line.split()  # split is used to check whether the Hex code are in braces{} or not
    if len(x)>1 and '{' not in x:  # Checks for elements are in Curve bracket or not
        m = re.findall(patt, input_line)
        [print(i) for i in m]  # is used to print all the elements in m usinf list comprehension
            
