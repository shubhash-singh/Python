import numpy
n = int(input())
# taking input for array A
A = numpy.array([input().split() for _ in range(n)], dtype=int)
# taking input for array B
B = numpy.array([input().split() for _ in range(n)], dtype=int)

print(numpy.dot(A, B))  # returns the dot product of Array A and B
print(numpy.cross(A, B))  # returns the cross product of Array A and B