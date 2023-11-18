import re

pattern = r"[.,]"  # to split if any , or . founds in a string into newline character

print('\n'.join(re.split(pattern, input())))