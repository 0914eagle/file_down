
def check_string(S):
    if len(S) < 4:
        return "WA"
    
    if S[0] != 'A':
        return "WA"
    
    if S.count('C') != 1:
        return "WA"
    
    for i in range(1, len(S) - 1):
        if i != 2 and i != len(S) - 2 and S[i].isupper():
            return "WA"
    
    return "AC"

# Reading input from Standard Input
S = input().strip()

# Checking the string and printing the result
print(check_string(S))
```
