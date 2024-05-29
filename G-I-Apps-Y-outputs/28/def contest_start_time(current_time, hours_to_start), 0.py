
def contest_start_time(current_time, hours_to_start):
    start_time = (current_time + hours_to_start) % 24
    return start_time

# Read input
current_time, hours_to_start = map(int, input().split())

# Calculate contest start time
start_time = contest_start_time(current_time, hours_to_start)

# Output the start time in 24-hour format
print(start_time)
```
