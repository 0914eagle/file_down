
def find_longest_sleep_time(n, alarms):
    alarms.sort()
    
    max_sleep_time = 0
    for i in range(n):
        next_alarm = alarms[(i + 1) % n]
        sleep_time = (next_alarm - alarms[i] - 1) % (24 * 60)
        if sleep_time > max_sleep_time:
            max_sleep_time = sleep_time
    
    hh = max_sleep_time // 60
    mm = max_sleep_time % 60
    
    return "{:02d}:{:02d}".format(hh, mm)

# Input
n = int(input())
alarms = []
for _ in range(n):
    h, m = map(int, input().split(':'))
    alarms.append(h * 60 + m)

# Output
print(find_longest_sleep_time(n, alarms))
```
