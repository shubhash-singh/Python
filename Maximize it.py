import itertools
# for finding the maximun from 3 list of integer
K, M = map(int, input().split())
# print(K, M)
N = []
for i in range(K):
    lst = list(map(int, input().split()))
    lst = lst[1:]
    N.append(lst)
    pro = list( itertools.product( *N ) )

maxi = 0
for item in pro:
    sum=0
    for num in item:
        sum += num**2
    modu = sum % M
    if (modu > maxi):
        maxi = modu
print(maxi)