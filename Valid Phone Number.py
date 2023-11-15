import re

pattern = r"7|8|9"

for i in range(int(input())):
    input_string = input()
    if input_string.isnumeric() and len(input_string) == 10:
        match = re.search(pattern, input_string[0])
        if match:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    
