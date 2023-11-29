import re

pat = r'\$\$'
for i in range(int(input())):
    string_input = input()
    output = re.sub("(?<=\s)&&(?=\s)", "and", string_input)
    output = re.sub("(?<=\s)\|\|(?=\s)", "or", output)
    print(output)
    