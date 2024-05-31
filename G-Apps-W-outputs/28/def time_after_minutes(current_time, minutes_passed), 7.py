
def time_after_minutes(current_time, minutes_passed):
    current_hours, current_minutes = map(int, current_time.split(':'))
    
    total_minutes = (current_hours * 60) + current_minutes + minutes_passed
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60
    
    return f"{new_hours:02d}:{new_minutes:02d}"

# Read input
current_time = input().strip()
minutes_passed = int(input().strip())

# Output result
print(time_after_minutes(current_time, minutes_passed))
