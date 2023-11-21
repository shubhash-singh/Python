import numpy
my_array = numpy.array([])
n, m = map(int, input().split())
for i in range(n):

    my_array += numpy.array(list(map(int, input().split())))

print(numpy.transpose(my_array))
print(my_array.flatten())
