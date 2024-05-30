
def min_arrow_keys_to_palindrome(n, p, s):
    p -= 1
    left = right = p
    moves = 0
    
    for i in range(n // 2):
        left_char = s[left]
        right_char = s[right]
        
        moves += min((ord(left_char) - ord(right_char)) % 26, (ord(right_char) - ord(left_char)) % 26)
        
        left = (left - 1) % n
        right = (right + 1) % n
    
    return moves

# Input
n, p = map(int, input().split())
s = input().strip()

# Output
print(min_arrow_keys_to_palindrome(n, p, s))
```
