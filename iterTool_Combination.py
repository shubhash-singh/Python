from itertools import combinations

input_str = input().split(" ")
Str = input_str[0]
n = int(input_str[1])
Str_array = []
for i in range(len(Str)):
    Str_array.append(Str[i])
Str_array.sort()

for i in range(1,n+1):
    result = combinations(Str_array,i)

    for a in result:
        print(''.join(a))
