import numpy
my_array = []  # creating a empty list
n, m = map(int, input().split())
for i in range(n):

    my_array.append(list(map(int, input().split())))
    # adding newly got input to aa list as a list element
my_array = numpy.array(my_array)  # creating multidimensional array
print(numpy.transpose(my_array))  # getting transpose of the array 
print(my_array.flatten())   # creating a single dimensional array from 2_D arary
