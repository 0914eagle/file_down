
def min_arrow_keys_to_palindrome(n, p, s):
    p -= 1  # Adjust 1-based index to 0-based index
    total_presses = 0
    
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
        total_presses += min(diff, 26 - diff)  # Calculate minimum presses to make characters equal
    
    dist = abs(p - n + 1) if p > n // 2 else p  # Calculate distance of cursor from the middle
    
    total_presses += min(dist, abs(n // 2 - p))  # Add minimum cursor movement to reach the middle
    
    return total_presses

# Input
n, p = map(int, input().split())
s = input()

# Output
print(min_arrow_keys_to_palindrome(n, p, s))
```
