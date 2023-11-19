from itertools import combinations


length = int(input())
str_input = input().split(" ")
Indicies = int(input())

output_String = list(combinations(str_input, Indicies))
occurance = list(filter(lambda c: 'a' in c, output_String)) 
# here filter is used to filter the values which matches the condition
# lambda is used to check the condition 
# lambda checks for occurance of 'a' in each element of output_String 
# output_String is a list of tuples and each tuples is iterated with c

print(len(occurance)/len(output_String))