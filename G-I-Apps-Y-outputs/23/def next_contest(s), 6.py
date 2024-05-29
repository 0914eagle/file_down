
def next_contest(s):
    if s == "ABC":
        return "ARC"
    elif s == "ARC":
        return "ABC"

S = input().strip()
print(next_contest(S))
```
