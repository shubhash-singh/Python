# a proogram to count the 3 most occuring number from a strig
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    char_count = Counter(sorted(s))
    common_count = char_count.most_common(3)
    for char, count in common_count:
        print(char, count)