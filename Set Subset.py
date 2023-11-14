# to check the subset of a set in multiple case
Test_number = int(input())

for i in range(Test_number):
    A_length = int(input())
    Set_A = set(map(int, input().split()))
    B_length = int(input())
    Set_B = set(map(int, input().split()))
    if Set_A <= Set_B:
        print(True)
    else:
        print(False)