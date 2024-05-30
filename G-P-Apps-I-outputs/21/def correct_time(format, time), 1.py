
def correct_time(format, time):
    hours, minutes = time.split(':')
    
    if format == 24:
        correct_hours = str(int(hours) % 24).zfill(2)
    else:
        correct_hours = str(int(hours) % 12).zfill(2)
        if correct_hours == '00':
            correct_hours = '12'
    
    correct_minutes = str(int(minutes) % 60).zfill(2)
    
    return f"{correct_hours}:{correct_minutes}"

# Input
format = int(input())
time = input()

# Output
print(correct_time(format, time))
```
