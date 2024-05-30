
def longest_sleep_time(n, alarms):
    alarms.sort()
    max_sleep_time = 0
    
    for i in range(n):
        start_time = alarms[i]
        end_time = alarms[(i + 1) % n]
        
        if end_time > start_time:
            duration = end_time - start_time - 1
        else:
            duration = (24 * 60 - start_time) + end_time - 1
        
        max_sleep_time = max(max_sleep_time, duration)
    
    return "{:02d}:{:02d}".format(max_sleep_time // 60, max_sleep_time % 60)

n = int(input())
alarms = []

for _ in range(n):
    hour, minute = map(int, input().split(':'))
    alarms.append(hour * 60 + minute)

print(longest_sleep_time(n, alarms))
```
