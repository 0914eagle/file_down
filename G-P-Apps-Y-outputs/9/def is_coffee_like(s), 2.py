
def is_coffee_like(s):
    if len(s) != 6:
        return "No"
    
    if s[2] == s[3] and s[4] == s[5]:
        return "Yes"
    else:
        return "No"

# Input reading
S = input().strip()

# Check if input is coffee-like
result = is_coffee_like(S)
print(result)
```
