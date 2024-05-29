
def check_property(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            return "No"
    return "Yes"

S = input().strip()
T = input().strip()

result = check_property(S, T)
print(result)
```
