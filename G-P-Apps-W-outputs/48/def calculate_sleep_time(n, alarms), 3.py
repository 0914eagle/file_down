
def calculate_sleep_time(n, alarms):
    alarms.sort()
    
    max_sleep_time = max((alarms[i] - alarms[i-1] - 1) % (24*60) for i in range(n) if alarms[i-1] < alarms[i])
    max_sleep_time = max(max_sleep_time, (alarms[0] - alarms[-1] - 1) % (24*60))
    
    hh = max_sleep_time // 60
    mm = max_sleep_time % 60
    
    return '{:02d}:{:02d}'.format(hh, mm)

# Read input
n = int(input())
alarms = []
for _ in range(n):
    h, m = map(int, input().split(':'))
    alarms.append(h*60 + m)

# Calculate and print the result
result = calculate_sleep_time(n, alarms)
print(result)
```
