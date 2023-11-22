import numpy

n, m = map(int, input().split())
N_list = []
for i in range(n):
    N_list.append(list(map(int, input().split())))
sum_output = numpy.sum(N_list, axis = 0) 
# this add both matrix to form a single matrix by adding each corresponding element so axis =0 is used
print(numpy.prod(sum_output))