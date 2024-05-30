
def next_tolerable_string(n, p, s):
    next_string = list(s)
    
    for i in range(n-1, -1, -1):
        next_char = chr(ord(next_string[i]) + 1)
        
        while next_char in s[:i] or (i > 0 and next_char == next_string[i-1]):
            next_char = chr(ord(next_char) + 1)
            if ord(next_char) > ord('a') + p - 1:
                next_char = ''
                break
        
        if next_char == '':
            continue
        
        for j in range(i, n):
            next_string[j] = next_char
        
        if ''.join(next_string) > s:
            return ''.join(next_string)
    
    return "NO"

# Input
n, p = map(int, input().split())
s = input().strip()

print(next_tolerable_string(n, p, s))
```
