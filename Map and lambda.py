cube = lambda x: x**3

def fibonacci(n):
    if n <1:
        return []
    elif n ==1:
        return [0]
    n1 = 0
    n2 = 1
    fab = [0, 1]
    for i in range(n-2):
        nth = n1+n2
        n1 = n2
        n2 = nth
        fab.append(nth)
    return fab

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))