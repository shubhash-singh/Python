def designer_door_mat(rows, columns):
    pattern = [('.|.' * (2 * i + 1)).center(columns, '-') for i in range(rows // 2)]
    welcome = 'WELCOME'.center(columns, '-')
    pattern = '\n'.join(pattern)
    
    print(pattern)
    print(welcome)
    print(pattern[::-1])

if __name__ == "__main__":
    n, m = map(int, input().split())
    designer_door_mat(n, m)