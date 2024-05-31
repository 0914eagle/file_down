
def find_time_after_minutes(current_time, minutes):
    hours, mins = map(int, current_time.split(':'))
    total_minutes = hours * 60 + mins + minutes
    hours_after = (total_minutes // 60) % 24
    mins_after = total_minutes % 60
    return f"{hours_after:02d}:{mins_after:02d}"

# Read input
current_time = input().strip()
minutes = int(input().strip())

# Find and print time after given minutes
print(find_time_after_minutes(current_time, minutes))
