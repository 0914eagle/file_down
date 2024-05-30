
def find_longest_sleep_time(n, alarms):
    alarms.sort()
    
    max_sleep_time = 0
    for i in range(n):
        if i == n - 1:
            diff = ((24 + alarms[0][0]) - alarms[i][1]) % 1440
        else:
            diff = (alarms[i+1][0] - alarms[i][1]) % 1440
        if diff > max_sleep_time:
            max_sleep_time = diff
    
    hours = max_sleep_time // 60
    minutes = max_sleep_time % 60
    
    return f"{hours:02d}:{minutes:02d}"

# Input reading
n = int(input())
alarms = []
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    alarms.append((hh*60 + mm, hh*60 + mm + 1))

print(find_longest_sleep_time(n, alarms))
```
