import numpy

n, m = map(int, input().split())
My_array = []
for i in range(n):
    My_array.append(list(map(int, input().split())))
min_array = numpy.min(My_array, axis=1)
# the above line will return an array of minimun value from each list
print(numpy.max(min_array))
# the above line will return a single maximum value from the array of munimun value
