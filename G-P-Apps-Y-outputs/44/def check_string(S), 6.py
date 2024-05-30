
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A' or S[2:-1].count('C') != 1:
        return "WA"
    
    for char in S[1:]:
        if char != 'a' and not char.islower():
            return "WA"
    
    return "AC"

S = input().strip()
print(check_string(S))
```
