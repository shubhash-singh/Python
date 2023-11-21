import numpy

n, m = map(int, input().split())
# we can use numpy.eye(a,b, k=c)
# to create a a x b matrix with c th diagonal element as 1
 
print(str(numpy.eye(n, m,k =0)).replace('1.', ' 1.').replace('0.', ' 0.'))
# using replace function for get an extra space before each element 
# to use .replace() 1st convert into string using str() fi=unction 