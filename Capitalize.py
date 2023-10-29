# Complete the solve function below.
def solve(s):
    for i in range(len(s)-1):
        if s[i] != " ":
            s=s[i+1:i+2].lower()
            
    return s
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
