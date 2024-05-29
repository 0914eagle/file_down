
def next_contest(last_contest):
    if last_contest == 'ABC':
        return 'ARC'
    elif last_contest == 'ARC':
        return 'ABC'

# Input
last_week_contest = input().strip()

# Output
print(next_contest(last_week_contest))
```
