
def find_time_after_minutes(current_time, a):
    hours, minutes = map(int, current_time.split(':'))
    
    total_minutes = hours * 60 + minutes + a
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60
    
    return f"{new_hours:02d}:{new_minutes:02d}"

# Read input
current_time = input().strip()
a = int(input().strip())

# Find and print the time after a minutes
result = find_time_after_minutes(current_time, a)
print(result)
