
def min_arrow_keys_to_palindrome(n, p, s):
    p -= 1
    operations = 0
    
    for i in range(n // 2):
        left_dist = (p - i + n) % n
        right_dist = (i - p + n) % n
        
        min_dist = min(left_dist, right_dist)
        
        operations += min_dist
        
        if s[p] != s[(p + min_dist) % n]:
            operations += min(abs(ord(s[p]) - ord(s[(p + min_dist) % n])), 26 - abs(ord(s[p]) - ord(s[(p + min_dist) % n])))
        
        p = (p + min_dist) % n
    
    return operations

# Input
n, p = map(int, input().split())
s = input().strip()

# Output
print(min_arrow_keys_to_palindrome(n, p, s))
```
