# performing mathmatical operation on array using numpy

import numpy as np

N, M = map(int, input().split())
for i in range(N):
    Array_A = np.array(list(map(int, input().split())))
    Array_B = np.array(list(map(int, input().split())))
    print(np.add(Array_A, Array_B))
    # to add two matrix aslo can be done by Array_A + Array_B
    print(np.subtract(Array_A, Array_B))
    # to subtract two matrix also can be done by Array_A - Array_B
    print(np.multiply(Array_A, Array_A))
    # multiplication of two matrix also can be done by Array_A * Array_B
    print(np.floor_divide(Array_A, Array_B))
    # integer division of two matrix also can be done by Array_A // Array_B
    print(np.mod(Array_A, Array_B))
    # modulous of two matrix also can be done by Array_A % Array_B
    print(np.power(Array_A, Array_B))
    # taking Array_B as power of Array_A also can be done by Array_A ** Array_B