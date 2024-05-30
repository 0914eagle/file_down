
def next_tolerable_string(n, p, s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    next_char = lambda c: alphabet[(alphabet.index(c) + 1) % p]

    for i in range(n-1, -1, -1):
        if s[i] != 'a' and (i == 0 or s[i-1] != next_char(s[i])):
            new_s = s[:i] + next_char(s[i]) + alphabet[0] * (n-i-1)
            if not any(new_s[j:j+2] == new_s[j+1:j+3][::-1] for j in range(n-1)):
                return new_s

    return "NO"


# Read input
n, p = map(int, input().split())
s = input().strip()

# Output
print(next_tolerable_string(n, p, s))
```
