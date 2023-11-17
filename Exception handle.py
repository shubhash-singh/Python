for i in range(int(input())):
    try:
        a, b = map(str, input().split())
        print(int(a)//int(b))
    except ValueError as e:  # To handle valueError If any character comes except integer
        print("Error Code:", e)
    except ZeroDivisionError as e:  # to handle error if there is 0 in denominator 
        print("Error Code:", e)
