def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        decimal = str(i)
        octal=oct(i)[2:]
        Hexadec = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {Hexadec.rjust(width)} {binary.rjust(width)}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)