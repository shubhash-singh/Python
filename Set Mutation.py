n = int(input())
Set_A = set(map(int, input().split()))

N = int(input())
for i in range(N):
    Command = input().split(" ")
    Set_B = set(map(int, input().split(" ")))
    if Command[0] == "intersection_update":
        Set_A.intersection_update(Set_B)
    elif Command[0] == "update":
        Set_A.update(Set_B)
    elif Command[0] == "difference_update":
        Set_A.difference_update(Set_B)
    elif Command[0] == "symmetric_difference_update":
        Set_A.symmetric_difference_update(Set_B)
# result = [a for a in Set_A]
print(sum(Set_A))