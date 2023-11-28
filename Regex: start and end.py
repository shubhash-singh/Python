import re

string = input()
sub_string = input()
pat = re.compile(sub_string)
m = pat.search(string)

if not m:
    print("-1,-1")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pat.search(string, m.start() + 1)