
def next_contest_type(last_week: str) -> str:
    return 'ARC' if last_week == 'ABC' else 'ABC'

# Input
S = input().strip()

# Output
print(next_contest_type(S))
```
