import numpy

ArrayA = numpy.array(input("Enter the Array").split(), float)
numpy.set_printoptions(sign=' ')  # to print an extra space between each element
print(numpy.floor(ArrayA))
# for getting the base of floating point number
# returns 1. if input is 1.34 or 1.1 or 1.8
print(numpy.ceil(ArrayA))
# returns the round value nearest to greatest or equlal to the value
# returns 2 for 1.1 or 1.9
print(numpy.rint(ArrayA))
# returns the round value
# returns 2 for 1.5 or above and returns 1 for 1.4 or below