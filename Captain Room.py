K = int(input())
room_list = list(map(int, input().split(" ")))

room_set = set(room_list)
Set_sum = sum(room_set) * K
Sum_all = sum(room_list)
Captain_Room = (Set_sum - Sum_all) // (K-1)
print(Captain_Room)