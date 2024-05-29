
def check_registration(S, T):
    if T == S + T[-1]:
        return "Yes"
    else:
        return "No"
    
S = input()
T = input()
print(check_registration(S, T))
```
