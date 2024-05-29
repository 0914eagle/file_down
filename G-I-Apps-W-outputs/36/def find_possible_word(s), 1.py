
def find_possible_word(s):
    if len(s) < 26:
        return -1

    for i in range(len(s) - 25):
        sub = s[i:i+26]
        if sub.count('?') + len(set(sub)) == 26 and all(c != '?' or sub.count(c) == 1 for c in set(sub)):
            missing_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(sub.replace('?', ''))
            for j in range(26):
                if sub[j] == '?':
                    sub = sub[:j] + missing_letters.pop() + sub[j+1:]
            return s[:i] + sub + s[i+26:]

    return -1

# Input
s = input().strip()

# Output
result = find_possible_word(s)
print(result)
```
