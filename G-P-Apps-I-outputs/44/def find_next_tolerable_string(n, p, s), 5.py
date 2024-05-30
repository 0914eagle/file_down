
def find_next_tolerable_string(n, p, s):
    def generate_next_char(char, p):
        next_char = chr(ord(char) + 1)
        while next_char in forbidden_chars or ord(next_char) - ord('a') >= p:
            next_char = chr(ord(next_char) + 1)
        return next_char
    
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    forbidden_chars = set()
    result = list(s)
    
    for i in range(n):
        if i < n - 1 and s[i] == s[i + 1]:
            forbidden_chars.add(s[i])
    
    for i in range(n - 1, -1, -1):
        current_char = result[i]
        next_char = generate_next_char(current_char, p)
        if next_char == 'z' and i > 0:
            result[i] = 'a'
            continue
        if i < n - 1 and next_char == result[i + 1]:
            forbidden_chars.add(next_char)
            next_char = generate_next_char(next_char, p)
        result[i] = next_char
        
    if any(is_palindrome(result[i:i+2]) for i in range(n-1)):
        return "NO"
    return ''.join(result)

# Reading input
n, p = map(int, input().split())
s = input().strip()

# Output the result
print(find_next_tolerable_string(n, p, s))
```
