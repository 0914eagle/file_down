
def correct_time(format, time):
    hours, minutes = map(int, time.split(":"))
    
    if format == 24:
        if hours > 23:
            hours %= 10
        if minutes > 59:
            minutes %= 10
    else:
        if hours > 12:
            hours %= 10
        if minutes > 59:
            minutes %= 10
        if hours == 0:
            hours = 1
    
    return f"{hours:02d}:{minutes:02d}"

# Read input
format = int(input())
time = input()

# Call the function and output the result
print(correct_time(format, time))
```
