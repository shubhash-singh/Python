import re
import email.utils

patt = r"^[a-z0-9][a-z0-9._-]*\@[a-z]+\.[a-z]{1,3}$"
for i in range(int(input())):
    name, input_e_mail = map(str, input().split(" "))
    emails = input_e_mail[1:-1]
    m = re.match(patt, emails, re.IGNORECASE)
    if m:
        print(email.utils.formataddr((name, emails)))