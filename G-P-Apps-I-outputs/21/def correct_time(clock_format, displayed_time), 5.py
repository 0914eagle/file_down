
def correct_time(clock_format, displayed_time):
    hours, minutes = displayed_time.split(':')
    
    if clock_format == 24:
        hours = str(int(hours) % 24).zfill(2)
    else:
        hours = str(int(hours) % 12).zfill(2)
        if hours == '00':
            hours = '12'
    
    minutes = str(int(minutes) % 60).zfill(2)
    
    return f"{hours}:{minutes}"

# Read input
clock_format = int(input())
displayed_time = input()

# Output corrected time
print(correct_time(clock_format, displayed_time))
```
