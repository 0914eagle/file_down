
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A':
        return "WA"
    
    if S[2:-1].count('C') != 1:
        return "WA"
    
    if not S[1:].islower():
        return "WA"
    
    return "AC"

S = input().strip()
result = check_string(S)
print(result)
```
