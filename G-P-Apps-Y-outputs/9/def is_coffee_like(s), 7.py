
def is_coffee_like(s):
    return "Yes" if s[2] == s[3] and s[4] == s[5] else "No"

# Read input from Standard Input
S = input().strip()

# Check if the input string is coffee-like
result = is_coffee_like(S)
print(result)
```
