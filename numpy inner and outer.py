import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B))  # returns the product of elements of two array
# a11*b11 + a12*b12 + c11+c12
print(np.outer(A, B))  # is equivalent to the matrix product of two array