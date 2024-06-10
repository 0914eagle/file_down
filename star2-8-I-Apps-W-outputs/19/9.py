
from collections import Counter

def is_nice(word):
    for i in range(len(word)-25):
        counter = Counter(word[i:i+26])
        if len(counter) == 26:
            return True
    return False

s = input()
if "?" not in s:
    if is_nice(s):
        print(s)
    else:
        print(-1)
else:
    missing_letters = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) - set(list(s))
    for letter in missing_letters:
        s = s.replace("?", letter, 1)
        if is_nice(s):
            print(s)
            break
    else:
        print(-1)


