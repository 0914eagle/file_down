
def find_longest_sleep_time(n, alarms):
    alarms.sort()
    
    max_sleep_time = 0
    for i in range(n):
        next_alarm = alarms[(i+1)%n]
        current_alarm = alarms[i]
        
        sleep_time = (next_alarm - current_alarm - 1) % (24*60)
        if sleep_time > max_sleep_time:
            max_sleep_time = sleep_time
    
    hh = max_sleep_time // 60
    mm = max_sleep_time % 60
    
    return f"{hh:02d}:{mm:02d}"

# Reading input
n = int(input())
alarms = []
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    total_minutes = hh * 60 + mm
    alarms.append(total_minutes)

print(find_longest_sleep_time(n, alarms))
```
