import numpy

# The poly tool returns the coefficients of a polynomial with the given sequence of roots.
print(numpy.poly([-1, 1, 1, 10]))        #Output : [  1 -11   9  11 -10]
# The roots tool returns the roots of a polynomial with the given coefficients.
print(numpy.roots([1, 0, -1]))           #Output : [-1.  1.]
# The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
print(numpy.polyint([1, 1, 1]))          #Output : [ 0.33333333  0.5         1.          0.        ]


P = list(map(float, input().split()))
x = int(input())
#  The polyval evaluates the polynomial at specific value which in our case is x
print(numpy.polyval(P, x))


# The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]