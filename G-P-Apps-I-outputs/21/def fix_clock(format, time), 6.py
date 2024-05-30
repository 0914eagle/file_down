
def fix_clock(format, time):
    hours = int(time[:2])
    minutes = int(time[3:])
    
    if format == 12:
        if hours > 12:
            hours -= 10
        if hours == 0:
            hours += 10
    else:
        if hours >= 24:
            hours -= 20
            
    if minutes >= 60:
        minutes -= 50
        
    return f"{hours:02d}:{minutes:02d}"

# Read input
format = int(input())
time = input().strip()

# Call the function and print the output
print(fix_clock(format, time))
```
