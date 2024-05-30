
def fix_clock(format, time):
    hours = int(time[:2])
    minutes = int(time[3:])
    
    if format == 24:
        if hours > 23:
            hours = hours % 10
        if minutes > 59:
            minutes = minutes % 10
    else:
        if hours > 12:
            hours = hours % 10
        if hours == 0:
            hours = 1
        if minutes > 59:
            minutes = minutes % 10
    
    return f"{hours:02d}:{minutes:02d}"

# Input parsing
format = int(input())
time = input()

# Call the function and print the result
print(fix_clock(format, time))
```
