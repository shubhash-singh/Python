from collections import deque
# perform various operation on deque
# deque is better version of list in which from both way we can append and pop
d = deque()
for i in range(int(input())):
    command = input().split()
    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    elif command[0] == "extend":
        d.extend(int(command[1]))
    elif command[0] == "extendleft":
        d.extend(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()

print(*d)