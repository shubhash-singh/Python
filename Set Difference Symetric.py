len_a = int(input())
a_input = input().split(" ")
len_b = int(input())
b_input = input().split(" ")
# print(a_input, b_input)
set_a = set(a_input)
set_b = set(b_input)
result1 = set_a-set_b
result2 = set_b-set_a
for a in result2:
    result1.add(a)
'''for b in sorted(result1):
    print(int(b))'''
result1 = set(int(a) for a in result1)
for i in sorted(result1):
    print(i)