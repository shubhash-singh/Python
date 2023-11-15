# to check a Super set (Strict Subset)

set_A = set(input().split())
N = int(input())
result = 0
count = 0
for i in range(N):
    if set_A.issuperset(input().split()): # and len(set_A) > len(SubSet):
        result += 1
    else:
        count += 1
if count != 0:
    print(False)
else:
    print(True)
