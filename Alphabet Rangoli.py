def print_rangoli(size):
    n = size

    # Create a list of alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create the upper part of the rangoli
    for i in range(n - 1, 0, -1):
        row = '-'.join(alphabet[n - 1:i:-1] + alphabet[i:n])
        print(row.center(n * 4 - 3, '-'))

    for i in range(0, n):
        row = '-'.join(alphabet[n - 1:i:-1] + alphabet[i:n])
        print(row.center(n * 4 - 3, '-'))
        
if __name__ == '__main__':
    n = int(input("Enter the size: "))
    print_rangoli(n)