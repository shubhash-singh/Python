from itertools import combinations_with_replacement

input_str = input().split(" ")
Str = input_str[0]
n = int(input_str[1])
Str_array = []
for i in range(len(Str)):
    Str_array.append(Str[i])
Str_array.sort()


result = combinations_with_replacement(Str_array, n)

for a in result:
    print(''.join(a))
