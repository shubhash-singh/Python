#taking list operation as a command from user
if __name__ == '__main__':
    N = int(input())
    arr=[]
    while (N!=0):
        command = input()
        command=command.split(" ")
        if command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(arr)
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "reverse":
            arr.reverse()
        elif command[0] == "pop":
            arr.pop()
        
        N=N-1