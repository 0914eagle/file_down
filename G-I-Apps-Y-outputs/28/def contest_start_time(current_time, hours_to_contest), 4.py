
def contest_start_time(current_time, hours_to_contest):
    return (current_time + hours_to_contest) % 24

A, B = map(int, input().split())
print(contest_start_time(A, B))
```
