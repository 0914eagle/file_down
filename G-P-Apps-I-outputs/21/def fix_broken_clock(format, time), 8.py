
def fix_broken_clock(format, time):
    hours, minutes = time.split(':')
    if format == 12:
        hours = int(hours) % 12
        if hours == 0:
            hours = 12
    else:
        hours = int(hours) % 24

    minutes = int(minutes) % 60

    return f"{hours:02d}:{minutes:02d}"

# Read input
format = int(input())
time = input().strip()

# Call the function and print the output
print(fix_broken_clock(format, time))
```
