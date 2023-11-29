def vowel_count(word):
    letter = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel = 0
    for w in word:
        if w in letter:
            vowel += 1
    if vowel % 2==0:
        return 2
    else:
        return 1
        
    
def score_words(words):
    score = 0
    for word in words:
        no_of_vowel = vowel_count(word)
        if no_of_vowel == 1:
            score += 1
        else:
            score += 2
    return score


n = int(input())
words = input().split()
print(score_words(words))