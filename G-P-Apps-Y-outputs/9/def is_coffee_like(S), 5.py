
def is_coffee_like(S):
    if len(S) != 6:
        return "No"

    if S[2] == S[3] and S[4] == S[5]:
        return "Yes"
    else:
        return "No"

# Read input
S = input().strip()

# Check if S is coffee-like
result = is_coffee_like(S)
print(result)
```
