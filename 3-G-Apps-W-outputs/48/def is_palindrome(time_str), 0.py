
def is_palindrome(time_str):
    return time_str == time_str[::-1]

def find_min_sleep_time(current_time):
    hh, mm = map(int, current_time.split(':'))
    total_minutes = hh * 60 + mm

    while True:
        total_minutes = (total_minutes + 1) % (24 * 60)
        hh = total_minutes // 60
        mm = total_minutes % 60
        time_str = f"{hh:02d}:{mm:02d}"
        
        if is_palindrome(time_str):
            return (total_minutes - (hh * 60 + mm))

# Input
current_time = input().strip()

# Output
print(find_min_sleep_time(current_time))
