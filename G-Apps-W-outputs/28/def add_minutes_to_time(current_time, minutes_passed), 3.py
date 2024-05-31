
def add_minutes_to_time(current_time, minutes_passed):
    hours, minutes = map(int, current_time.split(':'))
    total_minutes = hours * 60 + minutes + minutes_passed
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60
    return f"{new_hours:02d}:{new_minutes:02d}"

# Read input
current_time = input()
minutes_passed = int(input())

# Get and print the time after a minutes
new_time = add_minutes_to_time(current_time, minutes_passed)
print(new_time)
