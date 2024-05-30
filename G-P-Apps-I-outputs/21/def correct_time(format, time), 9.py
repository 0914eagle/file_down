
def correct_time(format, time):
    hours, minutes = time.split(':')
    
    if format == 12:
        if int(hours) > 12:
            hours = str(int(hours) % 10) + hours[1]
        
        if int(hours) == 0:
            hours = '01'
            
    elif format == 24:
        if int(hours) > 23:
            hours = '0' + hours[1]
    
    if int(minutes) > 59:
        minutes = '0' + minutes[1]
    
    return hours + ':' + minutes

# Input
format = int(input())
time = input()

# Output
print(correct_time(format, time))
```
