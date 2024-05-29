
def check_string_property(S, T):
    if T.startswith(S) and T[len(S)] != S[-1]:
        return "Yes"
    else:
        return "No"

S = input().strip()
T = input().strip()
result = check_string_property(S, T)
print(result)
```
