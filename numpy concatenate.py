import numpy

n, m, p = map(int, input().split())
n_list = []
m_list = []
for i in range(n):
    n_list.append(list(map(int, input().split())))
for i in range(m):
    m_list.append(list(map(int, input().split())))
array_1 = numpy.array(n_list)
array_2 = numpy.array(m_list)
# print(array_1, "\n\n\n", array_2)
print(numpy.concatenate((array_1, array_2), axis=0))