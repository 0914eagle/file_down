
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A':
        return "WA"
    
    count_C = 0
    for i in range(2, len(S)-1):
        if S[i] == 'C':
            count_C += 1
    
    if count_C != 1:
        return "WA"
    
    for char in S[1:]:
        if char.isupper() and char != 'C':
            return "WA"
    
    return "AC"

S = input().strip()
print(check_string(S))
```
