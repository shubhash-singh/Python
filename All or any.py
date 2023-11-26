N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))
# this print function print true if both condition are true 
# using any and all function to check for conditions