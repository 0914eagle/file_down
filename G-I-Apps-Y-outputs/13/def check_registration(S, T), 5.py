
def check_registration(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            return "No"
    return "Yes"

S = input().strip()
T = input().strip()

print(check_registration(S, T))
```
