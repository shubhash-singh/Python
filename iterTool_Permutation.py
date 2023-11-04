from itertools import combinations_with_replacement

input_string = input()
S = input_string.split(" ")
n = int(S[1])
STR = S[0]

result=[]

result = combinations_with_replacement(STR,2)
for a in result:
    print(''.join(a))