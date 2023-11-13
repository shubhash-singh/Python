# set Difference
n = int(input())
set1 = set(map(int, input().split(" ")))
m = int(input())
set2 = set(map(int, input().split(" ")))

result = set1 - set2
print(len(result))


# set Symetric Difference
n = int(input())
set1 = set(map(int, input().split(" ")))
m = int(input())
set2 = set(map(int, input().split(" ")))

result = set1 & set2
print(len(result))