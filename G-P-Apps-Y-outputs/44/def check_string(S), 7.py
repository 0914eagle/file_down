
def check_string(S):
    if len(S) < 4 or len(S) > 10:
        return "WA"

    if S[0] != 'A':
        return "WA"
    
    if S.count('C') != 1:
        return "WA"

    for i in range(1, len(S)-1):
        if S[i] != 'C' and (not S[i].islower()):
            return "WA"
    
    return "AC"

S = input().strip()
print(check_string(S))
```
