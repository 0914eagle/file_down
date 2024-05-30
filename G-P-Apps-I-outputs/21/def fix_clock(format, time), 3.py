
def fix_clock(format, time):
    hours, minutes = map(int, time.split(':'))
    if format == 12:
        hours %= 12
        if hours == 0:
            hours = 12
    else:
        hours %= 24

    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)

    return f"{hours}:{minutes}"

# Read input
format = int(input())
time = input()

# Call the function and print the output
print(fix_clock(format, time))
```
