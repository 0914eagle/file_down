
def max_sleep_time(n, alarms):
    alarms.sort()
    
    max_sleep = 0
    sleep_start = alarms[-1]
    
    for i in range(n):
        sleep_end = alarms[i - 1] if i > 0 else (24, 0)
        time_diff = ((sleep_start[0] - sleep_end[0] - 1) % 24) * 60 + (60 - sleep_end[1]) + sleep_start[1]
        if time_diff > max_sleep:
            max_sleep = time_diff
    
    return "{:02d}:{:02d}".format(max_sleep // 60, max_sleep % 60)

n = int(input())
alarms = []
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    alarms.append((hh, mm))

print(max_sleep_time(n, alarms))
```
