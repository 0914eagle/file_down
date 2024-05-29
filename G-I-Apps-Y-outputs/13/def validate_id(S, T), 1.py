
def validate_id(S, T):
    if T.startswith(S):
        return "Yes"
    else:
        return "No"

S = input().strip()
T = input().strip()

print(validate_id(S, T))
```
