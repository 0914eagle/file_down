
def find_longest_sleep_time(n, alarms):
    alarms.sort()
    max_sleep_time = 0
    for i in range(n):
        sleep_time = (alarms[(i + 1) % n] - alarms[i] - 1) % (24 * 60)
        max_sleep_time = max(max_sleep_time, sleep_time)
    hours = max_sleep_time // 60
    minutes = max_sleep_time % 60
    return f"{hours:02d}:{minutes:02d}"

# Input reading
n = int(input())
alarms = []
for _ in range(n):
    alarm = input().split(':')
    hours, minutes = int(alarm[0]), int(alarm[1])
    alarms.append(hours * 60 + minutes)

print(find_longest_sleep_time(n, alarms))
```

