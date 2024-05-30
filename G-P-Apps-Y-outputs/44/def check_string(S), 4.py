
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A':
        return "WA"
    
    if S[2:-1].count('C') != 1:
        return "WA"
    
    for i in range(1, len(S)):
        if i != 2 and i != len(S) - 2 and not S[i].islower():
            return "WA"
    
    return "AC"

S = input().strip()
print(check_string(S))
```
