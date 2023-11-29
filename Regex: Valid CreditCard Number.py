import re

pat = r'^(?!.*(\d)(?:-?\1){3})[456]\d{3}\-*\d{4}\-*\d{4}\-*\d{4}$'


'''

(?!.*(\d)(?:-?\1){3})


    This part is a negative lookahead assertion, which is used to assert that a certain pattern does not appear ahead in the string. Let's break it down:

    ?!: This is the syntax for a negative lookahead assertion. It asserts that the pattern inside the lookahead does not match at the current position.

    .*: This part matches any sequence of characters (including none) because .* represents zero or more occurrences of any character.

    (\d): This part captures a single digit and remembers it using a capturing group.

    (?:-?\1){3}: This part is a non-capturing group (?: ... ) that matches three occurrences of the previously captured digit (\1) with optional hyphens (-) in between.
'''
for i in range(int(input())):
    card_number = input()
    result = re.match(pat, card_number)
    if result:
        print("Valid")
    else:
        print('Invalid')
        
# some time this will give valid for number like
# 6865---------------3965---------------1564-------------2918
# this can return valid as well need to solve this one later