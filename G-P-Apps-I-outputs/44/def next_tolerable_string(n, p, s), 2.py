
def next_tolerable_string(n, p, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def is_palindrome(s):
        return any(s[i:i+2] == s[i+1:i-1:-1] for i in range(len(s) - 1))
    
    def increment_string(s):
        curr = list(s)
        i = n - 1
        while i >= 0:
            curr[i] = alphabet[(alphabet.index(curr[i]) + 1) % p]
            if curr[i] != 'a':
                break
            i -= 1
        return ''.join(curr)
    
    while True:
        s = increment_string(s)
        if is_palindrome(s):
            continue
        return s if all(s[i] <= s[i+1] for i in range(n - 1)) else 'NO'

n, p = map(int, input().split())
s = input().strip()

result = next_tolerable_string(n, p, s)
print(result)
```
