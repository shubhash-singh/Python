'''
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''
# taking the input from user
s = input()

# using the lamnda function to filter and then sort
s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))

# printing the sorted string
print(*(s),sep = '')
