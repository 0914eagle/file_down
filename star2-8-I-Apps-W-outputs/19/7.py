
from collections import defaultdict

def solve(s):
    freq = defaultdict(int)
    for ch in s:
        if ch != "?":
            freq[ch] += 1
    
    missing_letters = []
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if freq[ch] == 0:
            missing_letters.append(ch)
    
    if len(missing_letters) > 0:
        for ch in s:
            if ch == "?":
                ch = missing_letters.pop()
                s = s.replace("?", ch, 1)
    
    return s

s = input()
print(solve(s))

