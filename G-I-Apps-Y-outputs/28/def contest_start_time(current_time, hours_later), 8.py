
def contest_start_time(current_time, hours_later):
    return (current_time + hours_later) % 24

A, B = map(int, input().split())
print(contest_start_time(A, B))
```
