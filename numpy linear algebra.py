import numpy
import math

n = int(input())
A = numpy.array([input().split() for _ in range(n)], dtype=float)
result = numpy.linalg.det(A)  # to calculate the determinant of the matrix
round_result = math.ceil(result * 10**2) / 10**2  # to round the value at 2 decimal place
print(round_result)



# The linalg.eig computes the eigenvalues and right eigenvectors of a square array. 

# vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
# print vals                                      #Output : [ 3. -1.]
# print vecs                                      #Output : [[ 0.70710678 -0.70710678]
#                                                 #Output : [ 0.70710678  0.70710678]]

# The linalg.inv tool computes the (multiplicative) inverse of a matrix.

# print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                 #Output : [ 0.66666667 -0.33333333]]
