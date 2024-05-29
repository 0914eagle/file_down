
def next_contest(last_contest):
    return 'ARC' if last_contest == 'ABC' else 'ABC'

S = input().strip()
print(next_contest(S))
```
