
def contest_start_time(current_time, hours_until_start):
    contest_time = (current_time + hours_until_start) % 24
    return contest_time

A, B = map(int, input().split())
result = contest_start_time(A, B)
print(result)
```
