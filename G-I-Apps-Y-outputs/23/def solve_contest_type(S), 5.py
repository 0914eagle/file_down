
def solve_contest_type(S):
    if S == 'ABC':
        return 'ARC'
    elif S == 'ARC':
        return 'ABC'

S = input().strip()
print(solve_contest_type(S))
```
