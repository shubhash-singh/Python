input_string = input()
count = 1
output_string = []

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i-1]:
        count+=1
    else:
        t1 = (count, int(input_string[i-1]))
        output_string.append(t1)
        count = 1
t2 = count, int(input_string[-1])
output_string.append(t2)
print(*output_string)