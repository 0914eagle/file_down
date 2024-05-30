
def is_palindrome(s):
    return s == s[::-1]

def next_tolerable_string(n, p, s):
    s = list(s)
    for i in range(n - 1, -1, -1):
        s[i] = chr(ord(s[i]) + 1)
        while s[i] in s[:i] or (i > 0 and s[i] == s[i - 1]):
            s[i] = chr(ord(s[i]) + 1)
        if ord(s[i]) <= ord('a') + p - 1:
            break
        s[i] = 'a'
    else:
        return "NO"
    
    for j in range(i + 1, n):
        s[j] = 'a'
        while s[j] in s[:j] or (j > 0 and s[j] == s[j - 1]):
            s[j] = chr(ord(s[j]) + 1)
    
    return ''.join(s)

# Input
n, p = map(int, input().split())
s = input().strip()

# Output
print(next_tolerable_string(n, p, s))
```
