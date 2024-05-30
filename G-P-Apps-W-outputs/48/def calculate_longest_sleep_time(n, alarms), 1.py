
def calculate_longest_sleep_time(n, alarms):
    alarms.sort()
    max_sleep_time = 0
    
    for i in range(n):
        next_alarm = alarms[(i + 1) % n]
        sleep_time = (next_alarm - alarms[i] - 1) % (24 * 60)
        if sleep_time > max_sleep_time:
            max_sleep_time = sleep_time
    
    hh = max_sleep_time // 60
    mm = max_sleep_time % 60
    return f"{hh:02d}:{mm:02d}"

# Input parsing
n = int(input())
alarms = []
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    alarms.append(hh * 60 + mm)

# Calculate and print the longest sleep time
print(calculate_longest_sleep_time(n, alarms))
```
