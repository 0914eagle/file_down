
def check_property(S, T):
    return T.startswith(S) and len(T) == len(S) + 1

S = input().strip()
T = input().strip()

if check_property(S, T):
    print("Yes")
else:
    print("No")
```
