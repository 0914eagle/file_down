
def find_time_after_minutes(current_time, minutes_passed):
    hours, minutes = map(int, current_time.split(':'))
    total_minutes = hours * 60 + minutes + minutes_passed
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60
    return f"{new_hours:02d}:{new_minutes:02d}"

# Read input
current_time = input().strip()
minutes_passed = int(input().strip())

# Print output
print(find_time_after_minutes(current_time, minutes_passed))
