from collections import OrderedDict

ordered_dict = OrderedDict()
for i in range(int(input())):
    item, space, price = input().rpartition(' ')  
    # in above line the repartition function is spliting the value of input into three part
    # it convert a string into 3 part which are
    # 1st part where all value upto last occurance of seperator is stored
    # 2nd part store the seperator 
    # and third part store all value after the last occurance of seperator 
    
    ordered_dict[item] = ordered_dict.get(item, 0) + int(price)

for item, price in ordered_dict.items():
    print(item, price)    
    