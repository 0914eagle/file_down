
def next_contest_type(last_contest):
    return "ARC" if last_contest == "ABC" else "ABC"

last_contest = input().strip()
print(next_contest_type(last_contest))
```
