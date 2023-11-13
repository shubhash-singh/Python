m, n = map(int, input().split())
Array = list(map(int, input().split(" ")))
set1 = set(map(int, input().split(" ")))
set2 = set(map(int, input().split(" ")))
happiness = 0

for elem in Array:
    if elem in set1:
        happiness +=1
    
    if elem in set2:
        happiness -= 1
print(happiness)
        
