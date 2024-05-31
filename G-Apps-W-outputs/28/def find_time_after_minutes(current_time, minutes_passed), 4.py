
def find_time_after_minutes(current_time, minutes_passed):
    hh, mm = map(int, current_time.split(':'))
    total_minutes = hh * 60 + mm + minutes_passed
    new_hh = (total_minutes // 60) % 24
    new_mm = total_minutes % 60
    return f"{new_hh:02d}:{new_mm:02d}"

# Read input
current_time = input().strip()
minutes_passed = int(input().strip())

# Find and print the time after the given minutes
print(find_time_after_minutes(current_time, minutes_passed))
