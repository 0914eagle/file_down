
def contest_start_time(current_time, hours_to_start):
    return (current_time + hours_to_start) % 24

A, B = map(int, input().split())
start_time = contest_start_time(A, B)
print(start_time)
```
