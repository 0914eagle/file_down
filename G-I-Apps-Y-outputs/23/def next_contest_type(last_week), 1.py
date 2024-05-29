
def next_contest_type(last_week):
    if last_week == "ABC":
        return "ARC"
    elif last_week == "ARC":
        return "ABC"

# Input
S = input().strip()

# Output
print(next_contest_type(S))
```
