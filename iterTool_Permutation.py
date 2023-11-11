from itertools import permutations

input_string = input()
S = input_string.split(" ")
n = int(S[1])
STR = S[0]

result=[]
arranged_result = []
result = permutations(STR,n)
#print(result)

for a in result:
    arranged_result.append(''.join(a))
    
arranged_result.sort()
for b in arranged_result:
    print(b)
    