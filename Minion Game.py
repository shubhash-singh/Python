def minion_game(string):
    vowel = "AEIOU"
    count_S=0
    count_K=0
    for i in range(len(string)):
        if string[i] in vowel:
            count_K+=len(string)-i
        else:
            count_S+=len(string)-i   
    if count_S>count_K: 
        print(f"Stuart {count_S}")
    elif count_S<count_K:
        print(f"Kevin {count_K}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)