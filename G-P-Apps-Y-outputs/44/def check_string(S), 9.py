
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A':
        return "WA"
    
    if S[2:-1].count('C') != 1:
        return "WA"
    
    for char in S[1:]:
        if char != 'A' and char != 'C' and not char.islower():
            return "WA"
    
    return "AC"

# Read input
S = input().strip()

# Check the string
result = check_string(S)
print(result)
```
