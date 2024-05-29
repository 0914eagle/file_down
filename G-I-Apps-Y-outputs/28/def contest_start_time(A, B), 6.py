
def contest_start_time(A, B):
    start_time = (A + B) % 24
    return start_time

A, B = map(int, input().split())
print(contest_start_time(A, B))
```
