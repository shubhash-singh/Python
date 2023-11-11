for i in range(1, int(input()) + 1):
    print('\n'.join([''.join(map(str, range(1, i + 1))) + ''.join(map(str, range(i - 1, 0, -1)))]))
