
def check_registration(S, T):
    if T.startswith(S) and len(T) == len(S) + 1:
        return 'Yes'
    else:
        return 'No'

S = input().strip()
T = input().strip()
print(check_registration(S, T))
```
