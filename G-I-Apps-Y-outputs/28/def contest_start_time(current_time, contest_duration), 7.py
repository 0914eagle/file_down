
def contest_start_time(current_time, contest_duration):
    start_time = (current_time + contest_duration) % 24
    return start_time

current_time, contest_duration = map(int, input().split())
print(contest_start_time(current_time, contest_duration))
```
