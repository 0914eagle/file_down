
def fix_clock(format, time):
    hours, minutes = map(int, time.split(':'))
    
    if format == 12:
        hours = hours % 12
        if hours == 0:
            hours = 12

    if hours > 23:
        hours = hours % 10
    if minutes > 59:
        minutes = minutes % 10

    return f"{hours:02d}:{minutes:02d}"

# Read input
format = int(input())
time = input()

# Output the fixed time
print(fix_clock(format, time))
```
