from collections import Counter

list_A = []
for i in range(int(input())):
    list_A.append(input())

result = Counter(list_A)
# the above line stores the each unique value as key and number of occurance as value in a dict
print(len(result))
print(*result.values())
# * is used to only print values
# if * is not used then "dict value" will also come in output
