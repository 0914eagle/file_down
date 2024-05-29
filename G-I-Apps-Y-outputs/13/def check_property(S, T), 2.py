
def check_property(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            if S[:i] == T[:i] and S[i:] == T[i+1:]:
                return "Yes"
            else:
                return "No"

S = input().strip()
T = input().strip()

print(check_property(S, T))
```
