m, n = map(int, input().split())
input_list = []
for i in range(n):
    A = list(map(float, input().split()))
    input_list += [A]
zipped = zip(*input_list)  # *input_list is there to create a zipped list of elements of input_list
for i in zipped:
    print(sum(i)/n)  # to get the average 