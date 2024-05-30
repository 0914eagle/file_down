
def max_sleep_time(n, alarms):
    alarms.sort()
    max_gap = alarms[0]
    for i in range(1, n):
        gap = (alarms[i] - alarms[i-1] - 1) % (24 * 60)
        if gap > max_gap:
            max_gap = gap
    last_gap = (alarms[0] - alarms[-1] - 1) % (24 * 60)
    if last_gap > max_gap:
        max_gap = last_gap
    return "{:02d}:{:02d}".format(max_gap // 60, max_gap % 60)

# Reading input
n = int(input())
alarms = []
for _ in range(n):
    hour, minute = map(int, input().split(':'))
    alarms.append(hour * 60 + minute)

print(max_sleep_time(n, alarms))
```
