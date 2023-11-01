import numpy as np

a= input()
arr= list(a.split(" "))
int_arr = [int(x) for x in arr]
my_arr = np.array(int_arr)
print(np.reshape(my_arr,(3,3)))
