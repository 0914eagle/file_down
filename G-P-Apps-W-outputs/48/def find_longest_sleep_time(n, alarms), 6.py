
def find_longest_sleep_time(n, alarms):
    max_sleep_time = 0
    alarms.sort()
    
    for i in range(n):
        next_alarm_time = alarms[(i + 1) % n]
        current_alarm_time = alarms[i]
        
        diff = (next_alarm_time - current_alarm_time + 1440) % 1440
        if diff > max_sleep_time:
            max_sleep_time = diff
    
    max_sleep_time -= 1
    hh = max_sleep_time // 60
    mm = max_sleep_time % 60
    
    return "{:02d}:{:02d}".format(hh, mm)

n = int(input())
alarms = []
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    alarms.append(hh * 60 + mm)

result = find_longest_sleep_time(n, alarms)
print(result)
```
