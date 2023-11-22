import numpy

n, m = map(int, input().split())
My_array = []
for i in range(n):
    My_array.append(list(map(int, input().split())))
mean_array = numpy.mean(My_array, axis=1)
# axis 1 used so it will retuen an array of mean value from each list
var_array = numpy.var(My_array, axis=0)
# The var tool computes the arithmetic variance along the specified axis
std_array = numpy.std(My_array)
# The std tool computes the arithmetic standard deviation along the specified axis

print(mean_array)
print(var_array)
numpy.set_printoptions(legacy='1.13')  # to set precision
print(std_array)