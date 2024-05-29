
def next_contest_type(last_week: str) -> str:
    if last_week == "ABC":
        return "ARC"
    else:
        return "ABC"

last_week = input().strip()
print(next_contest_type(last_week))
```
