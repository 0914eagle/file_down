
def check_id_property(S, T):
    if T.startswith(S):
        return "Yes"
    else:
        return "No"

S = input().strip()
T = input().strip()
print(check_id_property(S, T))
```
