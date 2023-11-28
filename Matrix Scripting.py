import re

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = input()
    matrix.append(list(j for j in row))
semi_output_string = ""
# print(*matrix)
j = 0
for j in range(m):
    for i in matrix:
        semi_output_string += i[j]
pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
result = re.sub(pattern, ' ', semi_output_string)  # to substitute all apecial character with ' '
print(result)