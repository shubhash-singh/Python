from collections import Counter

shoes_no = int(input())
size = input()
str_size = size.split(" ")
shoes_size = [int(i) for i in str_size]
available_shoes = Counter(shoes_size)
earning = 0
shoes_price = {}
costu_no = int(input())
for i in range(0, costu_no):
    c1 = input()
    str_list = c1.split(" ")
    int_list = [int(x) for x in str_list]
    for j in available_shoes.keys():
        if int_list[0] == j and available_shoes[j] > 0:
            earning+=int_list[1]
            available_shoes[j] -= 1
        
print(earning)