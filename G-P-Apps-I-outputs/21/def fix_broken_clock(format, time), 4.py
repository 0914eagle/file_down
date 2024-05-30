
def fix_broken_clock(format, time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)

    if format == 12:
        if hours > 12:
            hours -= 12
    else:
        if hours > 23:
            hours = hours % 10
        if minutes > 59:
            minutes = minutes % 10

    return "{:02d}:{:02d}".format(hours, minutes)

# Input parsing
format = int(input())
time = input()

result = fix_broken_clock(format, time)
print(result)
```
