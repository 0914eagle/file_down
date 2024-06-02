
def is_palindrome(time_str):
    return time_str == time_str[::-1]

def find_next_palindrome_time(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh = (hh + 1) % 24
        time_str = f"{hh:02d}:{mm:02d}"
        if is_palindrome(time_str):
            return time_str

def min_sleep_time(current_time):
    if is_palindrome(current_time):
        return 0

    next_palindrome_time = find_next_palindrome_time(current_time)
    hh, mm = map(int, current_time.split(':'))
    next_hh, next_mm = map(int, next_palindrome_time.split(':'))

    minutes_diff = (next_hh - hh) * 60 + (next_mm - mm)
    if minutes_diff < 0:
        minutes_diff += 24 * 60

    return minutes_diff

# Input
current_time = input().strip()

# Output
print(min_sleep_time(current_time))
