# def is_palindromic(list1):
#     list1 = str(list1)
#     if list1 == list1[::-1]:
#         return True
#     else:
#         return False

# a = int(input())
# list1 = list(map(int, input().split()))
# print(list1)
# if all(a>0 for a in list1):
#     if any(is_palindromic(elem) for elem in list1):
#         print(True)
# else:
#     print(False)

N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))